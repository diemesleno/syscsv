from django.test import TestCase
from django.test import RequestFactory

from sys2.core.views import IndexView


class TestIndexView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = IndexView.as_view()
    
    def test_get(self):
        request = self.factory.get('/')
        response = self.view(request)
        self.assertEquals(200, response.status_code)
