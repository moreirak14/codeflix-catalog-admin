from uuid import uuid4

import pytest

from src.core.category.application.exceptions import NotFoundCategoryError
from src.core.category.application.get_category import (
    GetCategory,
    GetCategoryRequest,
    GetCategoryResponse,
)
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestGetCategory:
    def test_get_category_by_id(self):
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

        use_case = GetCategory(repository=repository)
        request = GetCategoryRequest(
            id=category_1.id,
        )

        response = use_case.execute(request)

        assert response == GetCategoryResponse(
            id=category_1.id,
            name=category_1.name,
            description=category_1.description,
            is_active=category_1.is_active,
        )

    def test_when_category_does_not_found_then_raise_exception(self):
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

        use_case = GetCategory(repository=repository)

        not_found_id = uuid4()

        request = GetCategoryRequest(
            id=not_found_id,
        )

        with pytest.raises(NotFoundCategoryError):
            use_case.execute(request)
