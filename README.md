Rails style controller dispatch method for Django class based views. Instead
of dispatching incoming http request to HTTP verbs such as 'GET', 'POST',
'DELETE' etc, it dispatch to more familiar CRUD action such as create, update,
delete, and delete. For browser based apps, I found the CRUD action make
more sense, after all in the browser we only limited to GET and POST so not much gain to split our request handler into proper HTTP method.

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
