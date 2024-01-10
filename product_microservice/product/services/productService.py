from abc import ABC, abstractmethod
from typing import List, Optional
from ..repository import ProductRepository
from ..models import Product

class  ProductService(ABC):
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    @abstractmethod
    def find_all_products(self) -> List[Product]:
        return self.repository.find_all_products()

    @abstractmethod
    def find_product_by_id(self, product_id: int) -> Optional[Product]:
        return self.repository.find_product_by_id(product_id)

    @abstractmethod
    def create_product(self, product_data: dict) -> Product:
        return self.repository.create_product(product_data)

    @abstractmethod
    def update_product(self, product_id: int, product_data: dict) -> Optional[Product]:
        return self.repository.update_product(product_id, product_data)

    @abstractmethod
    def delete_product(self, product_id: int) -> bool:
        return self.repository.delete_product(product_id)

    @abstractmethod
    def search_products(self, keyword: str) -> bool:
        return self.repository.search_products(keyword)
