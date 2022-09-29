from django.test import TestCase, Client
from django.urls import resolve

# Create your tests here.
class MyTest(TestCase):
    def test_html(self):
        response = Client().get("/mywatchlist/html", follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_xml(self):
        response = Client().get("/mywatchlist/xml", follow=True)
        self.assertEqual(response.status_code, 200)

    def test_json(self):
        response = Client().get("/mywatchlist/json", follow=True)
        self.assertEqual(response.status_code, 200)