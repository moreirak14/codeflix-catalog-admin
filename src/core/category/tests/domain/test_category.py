from uuid import UUID

import pytest

from src.core.category.domain.category import Category


class TestCategory:
    def test_name_is_required(self):
        with pytest.raises(
            TypeError, match="missing 1 required positional argument: 'name'"
        ):
            Category()

    def test_name_must_have_less_than_256_characters(self):
        with pytest.raises(
            ValueError, match="name must have less than 256 characters"
        ):
            Category("a" * 256)

    def test_name_cant_be_empty(self):
        with pytest.raises(ValueError, match="name can't be empty"):
            Category(name="")

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
        category = Category(
            name="name", description="description", is_active=False
        )
        assert category.id is not None
        assert isinstance(category.id, UUID)
        assert category.name == "name"
        assert category.description == "description"
        assert category.is_active is False


class TestUpdateCategory:
    def test_update_category(self):
        category = Category(name="name", description="description")

        category.update(name="new name", description="new description")

        assert category.name == "new name"
        assert category.description == "new description"

    def test_update_category_name_must_have_less_than_256_characters(self):
        category = Category(name="name", description="description")

        with pytest.raises(
            ValueError, match="name must have less than 256 characters"
        ):
            category.update(name="a" * 256, description="new description")

    def test_update_category_name_cant_be_empty(self):
        category = Category(name="name", description="description")

        with pytest.raises(ValueError, match="name can't be empty"):
            category.update(name="", description="new description")


class TestActivateCategory:
    def test_activate_category(self):
        category = Category(
            name="name", description="description", is_active=False
        )

        category.activate()

        assert category.is_active is True
