from django.test import TestCase
from django.urls import reverse

class TestViews(TestCase):

    def test_home_page(self):
        ''' Test home page renders '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
