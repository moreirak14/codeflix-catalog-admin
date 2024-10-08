from uuid import UUID

import pytest

from src.core.category.application.create_category import (
    InvalidCategoryDataError,
    create_category,
)


class TestCreateCategory:
    def test_create_category(self):
        category_id = create_category(
            name="name", description="description", is_active=True
        )

        assert category_id is not None
        assert isinstance(category_id, UUID)

    def test_create_category_with_invalid_data(self):
        with pytest.raises(
            InvalidCategoryDataError, match="name can't be empty"
        ) as error:
            create_category(
                name="",
            )

        assert error.type == InvalidCategoryDataError
        assert str(error.value) == "name can't be empty"
