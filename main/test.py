from django.test import Client
import unittest
from django.core.urlresolvers import reverse

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_effects(self):
        response = self.client.get('/effects/')
        self.assertEqual(response.status_code, 200)
        
    def test_meffects(self):
        response = self.client.get('/meffects/')
        self.assertEqual(response.status_code, 200)
        
    def test_manip(self):
        response = self.client.get(reverse("main:manip"))
        self.assertEqual(response.status_code, 302)
        
    def test_image(self):
        response = self.client.get(reverse("main:image"))
        self.assertEqual(response.status_code, 302)
        
    def test_save_effects(self):
        response = self.client.get(reverse("main:save_effects"))
        self.assertEqual(response.status_code, 302)
        
        
    def test_home(self):
        response = self.client.get(reverse("main:home"))
        self.assertEqual(response.status_code, 302)
        
  
