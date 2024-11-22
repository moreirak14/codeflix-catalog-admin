from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestSaveInMemoryCategoryRepository:
    def test_can_save_category(self):
        repository = InMemoryCategoryRepository()
        category = Category(
            name="name", description="description", is_active=True
        )

        repository.save(category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == category


class TestGetByIdInMemoryCategoryRepository:
    def test_can_get_category_by_id(self):
        category = Category(
            name="name", description="description", is_active=True
        )
        repository = InMemoryCategoryRepository(categories=[category])

        result = repository.get_by_id(id=category.id)

        assert result == category


class TestDeleteInMemoryCategoryRepository:
    def test_can_delete_category(self):
        category = Category(
            name="name", description="description", is_active=True
        )
        repository = InMemoryCategoryRepository(categories=[category])

        repository.delete(id=category.id)

        assert len(repository.categories) == 0
        assert repository.get_by_id(id=category.id) is None
