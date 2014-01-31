
from django.test import TestCase
from django.core.urlresolvers import reverse

class TestRouting(TestCase):
    def test_view(self):
        url = reverse('xxx')
        url = reverse('myview:retrieve', kwargs={'pk': '2'})
