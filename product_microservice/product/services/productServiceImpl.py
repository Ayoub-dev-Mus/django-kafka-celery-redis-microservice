from typing import List, Optional
from ..repository import ProductRepository
from .productService import ProductService
from ..models import Product

class ProductServiceImpl(ProductService):
    def __init__(self):
        super().__init__(ProductRepository())


    def find_all_products(self) -> List[Product]:
        return ProductRepository().find_all_products()

    def find_product_by_id(self, product_id: int) -> Optional[Product]:
        return ProductRepository().find_product_by_id(product_id)

    def create_product(self, product_data: dict) -> Product:
        return ProductRepository().create_product(product_data)

    def update_product(self, product_id: int, product_data: dict) -> Optional[Product]:
        return ProductRepository().update_product(product_id, product_data)

    def delete_product(self, product_id: int) -> bool:
        return ProductRepository().delete_product(product_id)

    def search_products(self, keyword: str) -> List[Product]:
        return ProductRepository().search_products(keyword)
