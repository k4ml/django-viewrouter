
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from viewrouter.views import ActionView
from viewrouter.routers import route

class MyView(ActionView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)
        
    @route(http_methods=['get'])
    def index(self, request):
        out = """
        <form action="." method="post">
        <input type="submit" value="submit" name="submit" />
        </form>
        """
        if request.method == 'POST':
            out += 'posted'
        return HttpResponse(out)

    def retrieve(self, request, pk):
        return HttpResponse('hello %d' % int(pk))

    def update(self, request, pk):
        return HttpResponse('update %d' % int(pk))
