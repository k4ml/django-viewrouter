
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf.urls import patterns, include, url

from viewrouter.routers import Router
from viewrouter.views import ActionView

class TestView(ActionView):
    urls = [
        ('^retrieve/%s/pass/$', 'retrieve', 'retrieve'),
    ]
    urls = []

    def index(self, request):
        return HttpResponse('index')

    def create(self, request):
        return HttpResponse('create')

    def retrieve(self, request, pk):
        return HttpResponse('hello %d' % int(pk))

    def update(self, request, pk):
        return HttpResponse('update %d' % int(pk))

    def delete(self, request, pk):
        return HttpResponse('delete %d' % int(pk))

test_router = Router(TestView)
urlpatterns = patterns('', url(r'', include(test_router.urls)))

class TestRouting(TestCase):
    urls = urlpatterns

    def test_view(self):
        url = reverse('testview:retrieve', kwargs={'pk': '2'})
        assert url == '/retrieve/2/', url
        url = reverse('testview:update', kwargs={'pk': '2'})
        assert url == '/update/2/', url
        url = reverse('testview:delete', kwargs={'pk': '2'})
        assert url == '/delete/2/', url
        url = reverse('testview:index')
        assert url == '/', url
        url = reverse('testview:create')
        assert url == '/create/', url

class TestRoutingOverride(TestCase):
    class TestView(ActionView):
        urls = [
            ('^retrieve/(?P<pk>\d+)/pass/$', 'retrieve', 'retrieve'),
        ]

        def retrieve(self, request, pk):
            return HttpResponse('hello %d' % int(pk))

    test_router = Router(TestView)
    urlpatterns = patterns('', url(r'', include(test_router.urls)))
    urls = urlpatterns

    def test_view(self):
        url = reverse('testview:retrieve', kwargs={'pk': '2'})
        assert url == '/retrieve/2/pass/', url
