
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.base import View

class ActionView(View):
    route_action = 'index'
    urls = []

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, self.route_action, self.not_found)
        else:
            handler = self.http_method_not_allowed

        return handler(request, *args, **kwargs)

    def not_found(self, *args, **kwargs):
        return HttpResponseNotFound()
