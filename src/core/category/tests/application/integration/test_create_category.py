from uuid import UUID

from src.core.category.application.create_category import (
    CreateCategory,
    CreateCategoryRequest,
)
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestCreateCategory:
    def test_create_category(self):
        repository = (
            InMemoryCategoryRepository()
        )  # SQLAlchemyCategoryRepository() or DjangoCategoryRepository()
        use_case = CreateCategory(repository=repository)
        request = CreateCategoryRequest(
            name="name", description="description", is_active=True
        )

        response = use_case.execute(request)

        assert response.id is not None
        assert isinstance(response.id, UUID)
        assert len(repository.categories) == 1
        assert repository.categories[0].id == response.id
        assert repository.categories[0].name == "name"
        assert repository.categories[0].description == "description"
        assert repository.categories[0].is_active is True
