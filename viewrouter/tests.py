
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf.urls import patterns, include, url

from viewrouter.routers import Router
from viewrouter.views import ActionView

class TestView(ActionView):
    def index(self, request):
        return HttpResponse('index')

    def retrieve(self, request, pk):
        return HttpResponse('hello %d' % int(pk))

    def update(self, request, pk):
        return HttpResponse('update %d' % int(pk))

test_router = Router(TestView)
urlpatterns = patterns('', url(r'', include(test_router.urls)))

class TestRouting(TestCase):
    urls = 'viewrouter.tests'

    def test_view(self):
        url = reverse('testview:retrieve', kwargs={'pk': '2'})
        assert url == '/retrieve/2/', url
        url = reverse('testview:update', kwargs={'pk': '2'})
        assert url == '/update/2/', url
        url = reverse('testview:index')
        assert url == '/', url
