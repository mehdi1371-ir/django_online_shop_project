from django.test import TestCase
from django.urls import reverse

class PagesTest(TestCase):

    def test_home_page_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name= 'home.html')

    def test_about_page_view(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name= 'pages/about.html')
