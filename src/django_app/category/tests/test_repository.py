import pytest

from django_app.category.models import CategoryModel
from django_app.category.repository import DjangoORMCategoryRepository


@pytest.mark.django_db
class TestSave:
    def test_save_category_in_database(self):
        category = CategoryModel(
            name="name",
            description="description",
            is_active=True,
        )

        repository = DjangoORMCategoryRepository()

        assert CategoryModel.objects.count() == 0

        repository.save(category)

        assert CategoryModel.objects.count() == 1

        category_saved = CategoryModel.objects.get(id=category.id)
        assert category_saved.name == category.name
        assert category_saved.description == category.description
        assert category_saved.is_active == category.is_active
        assert category_saved.id == category.id
