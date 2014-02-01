from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from myapp.views import ArticleView
from viewrouter.routers import Router

article_router = Router(ArticleView)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/', include(article_router.urls))
)
