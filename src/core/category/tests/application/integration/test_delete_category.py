from uuid import uuid4

import pytest

from src.core.category.application.exceptions import NotFoundCategoryError
from src.core.category.application.delete_category import (
    DeleteCategory,
    DeleteCategoryRequest,
)
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestDeleteCategory:
    def test_delete_category_by_id(self):
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

        repository = InMemoryCategoryRepository(
            categories=[category_1, category_2]
        )  # SQLAlchemyCategoryRepository() or DjangoCategoryRepository()

        use_case = DeleteCategory(repository=repository)
        request = DeleteCategoryRequest(
            id=category_1.id,
        )

        assert repository.get_by_id(id=category_1.id) == category_1

        use_case.execute(request)

        assert repository.get_by_id(id=category_1.id) is None
