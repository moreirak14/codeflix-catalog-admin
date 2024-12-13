import pytest
from rest_framework import status
from rest_framework.test import APIClient

from django_app.category.repository import DjangoORMCategoryRepository
from src.core.category.domain.category import Category


@pytest.mark.django_db
class TestCategoryAPI:
    @pytest.fixture
    def category_movie(self) -> Category:
        return Category(
            name="Movie",
            description="Movie description",
            is_active=True,
        )

    @pytest.fixture
    def category_electronic(self) -> Category:
        return Category(
            name="Electronic",
            description="Electronic description",
            is_active=True,
        )

    @pytest.fixture
    def category_repository(self) -> DjangoORMCategoryRepository:
        return DjangoORMCategoryRepository()

    def test_list_categories(
        self,
        category_movie: Category,
        category_electronic: Category,
        category_repository: DjangoORMCategoryRepository,
    ):
        category_repository.save(category_movie)
        category_repository.save(category_electronic)

        expected_data = [
            {
                "id": category_movie.id,
                "name": category_movie.name,
                "description": category_movie.description,
                "is_active": category_movie.is_active,
            },
            {
                "id": category_electronic.id,
                "name": category_electronic.name,
                "description": category_electronic.description,
                "is_active": category_electronic.is_active,
            },
        ]

        response = APIClient().get("/api/categories/")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2
        assert response.data == expected_data
