
from django.conf.urls import include, patterns, url

class Router(object):
    action_allowed = ['index', 'create', 'retrieve', 'update', 'delete']
    action_has_pk = ['retrieve', 'update', 'delete']
    
    def __init__(self, view, urls=None):
        self.view = view
        self.view_name = view.__name__.lower()
        self.urlpatterns = urls

    def build_urlpatterns(self, pattern, action, urlname, http_methods):
        kwargs = {
            'route_action': action,
        }
        if len(http_methods) > 0:
            kwargs['http_method_names'] = http_methods
        urlpatterns = patterns('',
            url(pattern, self.view.as_view(**kwargs), name=urlname)
        )
        return urlpatterns
    
    def build_default_pattern(self, action):
        if action in self.action_has_pk:
            pattern = r'^%s/(?P<pk>\d+)/$' % action
        else:
            pattern = r'^%s/$' % action
        return pattern
        
    @property
    def urls(self):
        urlpatterns = patterns('')
        overidden_actions = []
        for _url in self.view.urls:
            pattern, action, urlname, http_methods = _url
            overidden_actions.append(action)
            urlpatterns += self.build_urlpatterns(pattern, action, urlname, http_methods)

        for action in dir(self.view):
            if action not in self.action_allowed:
                continue
            if action in overidden_actions:
                continue

            action_callable = getattr(self.view, action, None)
            _urlname, _http_methods = None, []
            if action_callable is not None and hasattr(action_callable, '_route'):
                pattern, _urlname, _http_methods = action_callable._route
            else:
                pattern = self.build_default_pattern(action)

            # pattern still None, a case when user using @route decorator
            # but does not specify pattern
            if pattern is None:
                pattern = self.build_default_pattern(action)

            as_view_kwargs = {
                'route_action': action,
            }
            urlpatterns += self.build_urlpatterns(pattern, action, _urlname or action,
                                                  _http_methods)
            if action == 'index':
                urlpatterns += self.build_urlpatterns(r'^$', action, _urlname or action, _http_methods)
        return (urlpatterns, self.view_name, self.view_name)

def route(pattern=None, name=None, http_methods=None):
    def decorator(fn):
        fn._route = (pattern, name or fn.__name__, http_methods or [])
        return fn
    return decorator
