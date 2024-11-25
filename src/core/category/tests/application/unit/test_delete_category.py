from unittest.mock import create_autospec
from uuid import uuid4

import pytest

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.delete_category import (
    DeleteCategory,
    DeleteCategoryRequest,
)
from src.core.category.application.exceptions import NotFoundCategoryError
from src.core.category.domain.category import Category


class TestDeleteCategory:
    def test_delete_category(self):
        category = Category(
            name="name",
            description="description",
            is_active=True,
        )

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = category

        use_case = DeleteCategory(repository=mock_repository)
        use_case.execute(request=DeleteCategoryRequest(id=category.id))

        assert mock_repository.delete.called is True
        assert mock_repository.delete.call_count == 1

    def test_when_category_not_found_then_raise_exception(self):
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get_by_id.return_value = None

        use_case = DeleteCategory(repository=mock_repository)

        with pytest.raises(NotFoundCategoryError):
            use_case.execute(request=DeleteCategoryRequest(id=uuid4()))

        assert mock_repository.delete.called is False
        assert mock_repository.delete.call_count == 0
