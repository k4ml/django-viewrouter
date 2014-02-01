
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from viewrouter.views import ActionView
from viewrouter.routers import route

from myapp.models import ArticleForm, Article

class ArticleView(ActionView):
        
    @route(http_methods=['get'])
    def index(self, request):
        articles = Article.objects.all()
        ctx = {'articles': articles}
        return render(request, 'index.html', ctx)

    @route(http_methods=['get'])
    def create_form(self, request):
        form = ArticleForm()
        ctx = {'form': form}
        return render(request, 'create_form.html', ctx)

    @route(http_methods=['post'])
    def create(self, request):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articleview:index')

        ctx = {'form': form}
        return render(request, 'create_form.html', ctx)

    def retrieve(self, request, pk):
        return HttpResponse('hello %d' % int(pk))

    def update(self, request, pk):
        return HttpResponse('update %d' % int(pk))
