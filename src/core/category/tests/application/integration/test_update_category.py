from uuid import uuid4

import pytest

from src.core.category.application.exceptions import NotFoundCategoryError
from src.core.category.application.update_category import (
    UpdateCategory,
    UpdateCategoryRequest,
)
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestUpdateCategory:
    def test_update_category_name_and_description(self):
        category = Category(
            name="name",
            description="description",
            is_active=True,
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository=repository)
        request = UpdateCategoryRequest(
            id=category.id,
            name="new name",
            description="new description",
        )

        use_case.execute(request)

        updated_category = repository.get_by_id(id=category.id)

        assert updated_category.name == "new name"
        assert updated_category.description == "new description"
        assert updated_category.is_active is True

    def test_update_category_is_active(self):
        category = Category(
            name="name",
            description="description",
            is_active=True,
        )

        repository = InMemoryCategoryRepository()
        repository.save(category)

        use_case = UpdateCategory(repository=repository)
        request = UpdateCategoryRequest(
            id=category.id,
            is_active=False,
        )

        use_case.execute(request)

        updated_category = repository.get_by_id(id=category.id)

        assert updated_category.is_active is False

    def test_update_category_not_found(self):
        repository = InMemoryCategoryRepository()

        use_case = UpdateCategory(repository=repository)

        request = UpdateCategoryRequest(
            id=uuid4(),
            name="new name",
        )

        with pytest.raises(NotFoundCategoryError):
            use_case.execute(request)
