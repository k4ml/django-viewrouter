from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from myapp.views import MyView
from viewrouter.routers import Router

myapp_router = Router(MyView)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(myapp_router.urls))
)
