from uuid import UUID

from src.core.category.domain.category import Category


class InvalidCategoryDataError(Exception):
    pass


def create_category(
    name: str, description: str = None, is_active: bool = True
) -> UUID:
    try:
        category = Category(
            name=name, description=description, is_active=is_active
        )
    except ValueError as error:
        raise InvalidCategoryDataError(str(error)) from error

    return category.id
