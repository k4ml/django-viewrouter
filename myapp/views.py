
from django.http import HttpResponse, HttpResponseNotFound
from viewrouter.views import ActionView

class MyView(ActionView):
        
    def index(self, request):
        return HttpResponse('hello')

    def retrieve(self, request, pk):
        return HttpResponse('hello %d' % int(pk))

    def update(self, request, pk):
        return HttpResponse('update %d' % int(pk))
