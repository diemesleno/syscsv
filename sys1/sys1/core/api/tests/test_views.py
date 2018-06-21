from django.test import TestCase
from django.test import RequestFactory

from sys1.core.api.views import TaskResultAPIView


class TestTaskResultAPIView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.view = TaskResultAPIView.as_view()
    
    def test_get(self):
        request = self.factory.get('/')
        response = self.view(request)
        self.assertEquals(200, response.status_code)
