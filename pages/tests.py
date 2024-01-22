from django.test import SimpleTestCase
from django.urls import reverse

class HomepageTest(SimpleTestCase):
    """Test the home Page"""
    def test_url_exists_at_correct_location(self):
        """test url exists at correct location"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """test url available by name"""
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name is correct"""
        response=self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        """Test template content"""
        response=self.client.get(reverse("home"))
        self.assertContains(response, "<h1>Homepage</h1>")

class AboutpageTest(SimpleTestCase):
    """Test the about Page"""
    def test_url_exists_at_correct_location(self):
        """test url exists at correct location"""
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """test url available by name"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """test url available by name"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        """Test template name is correct"""
        response=self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        """Test template content"""
        response=self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")
  
