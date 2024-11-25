from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.exceptions import NotFoundCategoryError


@dataclass
class ListCategoryRequest:
    id: UUID


@dataclass
class CategoryOutput:
    id: UUID
    name: str
    description: str
    is_active: bool


@dataclass
class ListCategoryResponse:
    data: list[CategoryOutput]


class ListCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self) -> ListCategoryResponse:
        categories = self.repository.list()

        return ListCategoryResponse(
            data=[
                CategoryOutput(
                    id=category.id,
                    name=category.name,
                    description=category.description,
                    is_active=category.is_active,
                )
                for category in categories
            ]
        )