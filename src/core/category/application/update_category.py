from dataclasses import dataclass
from uuid import UUID

from src.core.category.application.category_repository import (
    CategoryRepository,
)
from src.core.category.application.exceptions import NotFoundCategoryError


@dataclass
class UpdateCategoryRequest:
    id: UUID
    name: str | None = None
    description: str | None = None
    is_active: bool | None = None


class UpdateCategory:
    def __init__(self, repository: CategoryRepository):
        self.repository = repository

    def execute(self, request: UpdateCategoryRequest) -> None:
        category = self.repository.get_by_id(id=request.id)

        if not category:
            raise NotFoundCategoryError(
                f"Category with ID {request.id} not found"
            )

        updated_name = request.name
        if updated_name is not None and updated_name != category.name:
            category.name = updated_name

        updated_description = request.description
        if updated_description is not None and updated_description != category.description:
            category.description = updated_description

        updated_is_active = request.is_active
        if updated_is_active is not None and updated_is_active != category.is_active:
            category.is_active = updated_is_active

        self.repository.update(category)
