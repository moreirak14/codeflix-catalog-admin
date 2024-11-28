from uuid import uuid4

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.request import Request
from rest_framework.response import Response


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    def list(self, request: Request) -> Response:
        return Response(
            data=[
                {
                    "id": uuid4(),
                    "name": "Category 1",
                    "description": "Category 1 description",
                    "is_active": True,
                },
                {
                    "id": uuid4(),
                    "name": "Category 2",
                    "description": "Category 2 description",
                    "is_active": True,
                },
            ],
            status=status.HTTP_200_OK
        )