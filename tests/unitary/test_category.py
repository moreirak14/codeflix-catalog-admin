import pytest
from uuid import UUID

from app.category import Category


class TestCategory:
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_less_than_256_characters(self):
        with pytest.raises(ValueError, match="name must have less than 256 characters"):
            Category("a" * 256)

    def test_category_must_be_created_with_id_and_as_uuid_by_default(self):
        category = Category(name="name")
        assert category.id is not None
        assert isinstance(category.id, UUID)

    def test_created_category_with_default_values(self):
        category = Category(name="name")
        assert category.id is not None
        assert isinstance(category.id, UUID)
        assert category.name == "name"
        assert category.description is None
        assert category.is_active is True

    def test_category_is_created_as_is_active_default(self):
        category = Category(name="name")
        assert category.is_active is True

    def test_category_is_created_with_provided_values(self):
        category = Category(name="name", description="description", is_active=False)
        assert category.id is not None
        assert isinstance(category.id, UUID)
        assert category.name == "name"
        assert category.description == "description"
        assert category.is_active is False
