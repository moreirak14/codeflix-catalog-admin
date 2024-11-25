from src.core.category.application.list_category import ListCategory, ListCategoryResponse, CategoryOutput
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import (
    InMemoryCategoryRepository,
)


class TestListCategory:
    def test_empty_list(self):
        repository = InMemoryCategoryRepository(categories=[])

        use_case = ListCategory(repository=repository)
        response = use_case.execute()

        assert response == ListCategoryResponse(data=[])

    def test_list_with_data(self):
        category_1 = Category(
            name="name",
            description="description",
            is_active=True,
        )
        category_2 = Category(
            name="name",
            description="description",
            is_active=True,
        )
        repository = InMemoryCategoryRepository()
        repository.save(category_1)
        repository.save(category_2)

        use_case = ListCategory(repository=repository)
        response = use_case.execute()

        assert response == ListCategoryResponse(
            data=[
                CategoryOutput(
                    id=category_1.id,
                    name=category_1.name,
                    description=category_1.description,
                    is_active=category_1.is_active,
                ),
                CategoryOutput(
                    id=category_2.id,
                    name=category_2.name,
                    description=category_2.description,
                    is_active=category_2.is_active,
                ),
            ],
        )


