Rails style controller dispatch method for Django class based views. Instead
of dispatching incoming http request to HTTP verbs such as 'GET', 'POST',
'DELETE' etc, it dispatch to more familiar CRUD action such as create, update,
delete, and delete. For browser based apps, I found the CRUD action make
more sense, after all in the browser we only limited to GET and POST so not much gain to split our request handler into proper HTTP method.

## Usage
Create a view class like below:-

```python
from django.http import HttpResponse
from viewrouter.views import ActionView

class ArticleView(ActionView):
    def index(self):
        return HttpResponse('this is index')

    def retrieve(self, pk):
        return HttpResponse('this is article %s' % pk)

    def delete(self, pk):
        return HttpResponse('deleting %s' % pk)

    def update(self, pk):
        return HttpResponse('updating %s' % pk)

```

Then in your `urls.py`:-

```python
from django.conf.urls import patterns, include, url
from viewrouter.routers import Router

from yourproject.views import ArticleView

article_router = Router(ArticleView)
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/', include(article_router.urls))
)
```
The following url now accessible:-

* /article/
* /article/index/ (similar to above)
* /article/update/<pk>/
* /article/retrieve/<pk>/
* /article/delete/<pk>/

By default the following methods on your class based views will be automatically routed:-

* `index`
* `retrieve`
* `update`
* `delete`
* `create`

Other methods can be routed by explicitly marking them with `route` decorator:-

```python
from django.http import HttpResponse
from viewrouter.views import ActionView
from viewrouter.routers import route

class ArticleView(ActionView):
    def index(self):
        return HttpResponse('this is index')

    def retrieve(self, pk):
        return HttpResponse('this is article %s' % pk)

    @route(r'^set-password/(?<user_id>\d+)/')
    def set_password(self, user_id):
        return HttpResponse('change password for user %s' % user_id)

```

Unlike django built-in class based views which route based on HTTP methods, this will route
all HTTP methods as long as the url pattern matched. To restrict the HTTP methods allowed,
use `http_methods`parameter to `@route` decorator:-

```python
    @route(r'^set-password/(?<user_id>\d+)/', http_methods=['post'])
    def set_password(self, user_id):
        return HttpResponse('change password for user %s' % user_id)

```

## Background
After start using class based views, I found our `urls.py` start getting cluttered with the boilerplate of wiring up the views into url patterns. And having split the views into proper http verbs, it mean we always need at least 2 separate
views to handle the CRUD operation. For example:-

```python
urlpatterns = patterns('',
        url(r'^article/$', ArticleView.as_view()),
        url(r'^article/(?P<pk>\d+)/$', ArticleEditorView.as_view()),
    )
```
Above, `ArticleView` will handle listing of articles and creating new one and
`ArticleEditorView` will handle updating, displaying single article and deleting
the article.
