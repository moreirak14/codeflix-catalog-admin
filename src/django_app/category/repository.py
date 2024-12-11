from abc import ABC
from uuid import UUID

from src.core.category.domain.category_repository import CategoryRepository
from src.core.category.domain.category import Category
from django_app.category.models import CategoryModel


class DjangoORMCategoryRepository(CategoryRepository, ABC):
    def __init__(self, category_model: CategoryModel = CategoryModel):
        self.model = category_model

    def save(self, category: Category) -> None:
        self.model.objects.create(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )

    def get_by_id(self, id: UUID) -> Category | None:
        try:
            category = self.model.objects.get(id=id)
            return Category(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active,
            )
        except self.model.DoesNotExist:
            return None

    def delete(self, id: UUID) -> None:
        self.model.objects.get(id=id).delete()

    def update(self, category: Category) -> None:
        self.model.objects.filter(id=category.id).update(
            name=category.name,
            description=category.description,
            is_active=category.is_active,
        )

    def list(self) -> list[Category]:
        categories = self.model.objects.all()
        return [
            Category(
                id=category.id,
                name=category.name,
                description=category.description,
                is_active=category.is_active,
            )
            for category in categories
        ]