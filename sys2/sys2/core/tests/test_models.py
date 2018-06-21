from django.test import TestCase

from model_mommy import mommy


class TestContact(TestCase):
    def setUp(self):
        self.models = mommy.make('core.Contact')
    
    def test_str(self):
        self.assertEquals(str(self.models), self.models.name)
