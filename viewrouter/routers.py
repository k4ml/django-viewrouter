
from django.conf.urls import include, patterns, url

class Router(object):
    action_allowed = ['index', 'create', 'retrieve', 'update', 'delete']
    action_has_pk = ['retrieve', 'update', 'delete']
    
    def __init__(self, view, urls=None):
        self.view = view
        self.view_name = view.__name__.lower()
        self.urlpatterns = urls

    @property
    def urls(self):
        urlpatterns = patterns('')
        for action in dir(self.view):
            if action not in self.action_allowed:
                continue
            if action in self.action_has_pk:
                pattern = r'^%s/(?P<pk>\d+)/$' % action
            else:
                pattern = r'^%s/$' % action

            urlpatterns += patterns('',
                url(pattern, self.view.as_view(route_action=action), name=action),
            )
            if action == 'index':
                urlpatterns += patterns('',
                    url(r'^$', self.view.as_view(route_action=action), name='index'),
                )
        return (urlpatterns, self.view_name, self.view_name)
