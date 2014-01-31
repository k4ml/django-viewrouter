
from django.conf.urls import include, patterns, url

class Router(object):
    
    def __init__(self, view, urls=None):
        self.view = view
        self.view_name = view.__name__.lower()
        self.urlpatterns = urls

    @property
    def urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.view.as_view(route_action='index'), name='index'),
            url(r'^index/$', self.view.as_view(route_action='index'), name='index'),
            url(r'^retrieve/(?P<pk>\d+)/$', self.view.as_view(route_action='retrieve'), name='retrieve'),
        )
        return (urlpatterns, self.view_name, self.view_name)
