from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.exceptions import NotFoundCategoryError
from src.core.category.domain.category_repository import (
    CategoryRepository,
)


@dataclass
class DeleteCategoryRequest:
    id: UUID


class DeleteCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: DeleteCategoryRequest) -> None:
        category = self.repository.get_by_id(id=request.id)

        if not category:
            raise NotFoundCategoryError(
                f"Category with ID {request.id} not found"
            )

        self.repository.delete(id=category.id)
