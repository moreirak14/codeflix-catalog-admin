from rest_framework.test import APITestCase


# Create your tests here.
class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        response = self.client.get(path="/api/categories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
