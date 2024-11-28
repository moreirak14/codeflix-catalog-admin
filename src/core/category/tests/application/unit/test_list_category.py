from unittest.mock import create_autospec

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.list_category import (
    CategoryOutput,
    ListCategory,
    ListCategoryResponse,
)
from src.core.category.domain.category import Category


class TestListCategory:
    def test_list_category(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.list.return_value = []

        use_case = ListCategory(repository=mock_repository)

        response = use_case.execute()

        assert response == ListCategoryResponse(
            data=[],
        )

    def test_list_category_with_data(self):
        category_1 = Category(
            name="name",
            description="description",
            is_active=True,
        )
        category_2 = Category(
            name="name",
            description="description",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.list.return_value = [category_1, category_2]

        use_case = ListCategory(repository=mock_repository)

        response = use_case.execute()

        assert response == ListCategoryResponse(
            data=[
                CategoryOutput(
                    id=category_1.id,
                    name=category_1.name,
                    description=category_1.description,
                    is_active=category_1.is_active,
                ),
                CategoryOutput(
                    id=category_2.id,
                    name=category_2.name,
                    description=category_2.description,
                    is_active=category_2.is_active,
                ),
            ],
        )
