
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.base import View

class MyView(View):
    route_action = 'index'

    def dispatch(self, request, *args, **kwargs):
        handler = getattr(self, self.route_action, self.not_found)
        return handler(request, *args, **kwargs)

    def not_found(self, *args, **kwargs):
        return HttpResponseNotFound()
        
    def index(self, request):
        return HttpResponse('hello')

    def retrieve(self, request, pk):
        return HttpResponse('hello %d' % int(pk))
