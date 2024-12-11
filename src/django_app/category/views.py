from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from django_app.category.repository import DjangoORMCategoryRepository
from src.core.category.application.list_category import (
    ListCategory,
    ListCategoryRequest,
)


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        input = ListCategoryRequest()

        use_case = ListCategory(repository=DjangoORMCategoryRepository())

        output = use_case.execute()

        categories = [
            {
                "id": category.id,
                "name": category.name,
                "description": category.description,
                "is_active": category.is_active,
            }
            for category in output.data
        ]

        return Response(
            status=status.HTTP_200_OK,
            data=categories,
        )
