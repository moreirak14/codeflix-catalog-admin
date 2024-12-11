from rest_framework.test import APITestCase

from django_app.category.repository import DjangoORMCategoryRepository
from src.core.category.domain.category import Category


# Create your tests here.
class TestCategoryAPI(APITestCase):
    def test_list_categories(self):
        category_1 = Category(
            name="name_1",
            description="description_1",
            is_active=True,
        )
        category_2 = Category(
            name="name_2",
            description="description_2",
            is_active=True,
        )

        repository = DjangoORMCategoryRepository()
        repository.save(category_1)
        repository.save(category_2)

        response = self.client.get(path="/api/categories/")

        expected_data = [
            {
                "id": str(category_1.id),
                "name": category_1.name,
                "description": category_1.description,
                "is_active": category_1.is_active,
            },
            {
                "id": str(category_2.id),
                "name": category_2.name,
                "description": category_2.description,
                "is_active": category_2.is_active,
            },
        ]

        response_data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data, expected_data)
        self.assertEqual(len(response_data), 2)
