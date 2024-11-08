from abc import ABC, abstractmethod

from src.core.category.domain.category import Category


class CategoryRepository(ABC):

    @abstractmethod
    def save(self, category: Category) -> None:
        raise NotImplementedError