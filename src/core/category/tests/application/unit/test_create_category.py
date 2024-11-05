from unittest.mock import MagicMock
from uuid import UUID

import pytest

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.create_category import (
    CreateCategory,
    CreateCategoryRequest,
)
from src.core.category.application.exceptions import InvalidCategoryDataError


class TestCreateCategory:
    def test_create_category(self):
        mock_repository = MagicMock(CategoryRepository)
        use_case = CreateCategory(repository=mock_repository)
        request = CreateCategoryRequest(
            name="name", description="description", is_active=True
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        mock_repository.save.assert_called_once()

    def test_create_category_with_invalid_data(self):
        mock_repository = MagicMock(CategoryRepository)

        use_case = CreateCategory(repository=mock_repository)

        request = CreateCategoryRequest(
            name="",
        )

        with pytest.raises(
            InvalidCategoryDataError, match="name can't be empty"
        ) as error:
            use_case.execute(request)

        assert error.type == InvalidCategoryDataError
        assert str(error.value) == "name can't be empty"
        mock_repository.save.assert_not_called()
