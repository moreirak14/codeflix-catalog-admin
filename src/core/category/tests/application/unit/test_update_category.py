from unittest.mock import create_autospec

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.update_category import (
    UpdateCategory,
    UpdateCategoryRequest,
)
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_update_category_name(self):
        category = Category(
            name="name",
            description="description",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="new name",
        )

        use_case.execute(request)

        assert category.name == "new name"
        assert mock_repository.update.called

    def test_update_category_description(self):
        category = Category(
            name="name",
            description="description",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)
        request = UpdateCategoryRequest(
            id=category.id,
            description="new description",
        )

        use_case.execute(request)

        assert category.description == "new description"
        assert mock_repository.update.called

    def test_update_category_is_active(self):
        category = Category(
            name="name",
            description="description",
            is_active=True,
        )
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = UpdateCategory(repository=mock_repository)

        assert category.is_active is True

        request = UpdateCategoryRequest(
            id=category.id,
            is_active=False,
        )

        use_case.execute(request)

        assert category.is_active is False
        assert mock_repository.update.called
