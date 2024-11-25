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


class TestUpdateInMemoryCategoryRepository:
    def test_can_update_category(self):
        category = Category(
            name="name", description="description", is_active=True
        )
        repository = InMemoryCategoryRepository(categories=[category])

        updated_category = Category(
            id=category.id,
            name="new name",
            description="new description",
            is_active=False,
        )

        repository.update(category=updated_category)

        assert len(repository.categories) == 1
        assert repository.categories[0] == updated_category


class TestListInMemoryCategoryRepository:
    def test_can_list_categories(self):
        category_1 = Category(
            name="name_1", description="description_1", is_active=True
        )
        category_2 = Category(
            name="name_2", description="description_2", is_active=True
        )
        repository = InMemoryCategoryRepository(
            categories=[category_1, category_2]
        )

        result = repository.list()

        assert result == [category_1, category_2]
