# repository.py
from .models import Product
from typing import List

class ProductRepository:
    def find_all_products(self) -> List[Product]:
        return Product.objects.all()

    def find_product_by_id(self, product_id: int) -> Product:
        return Product.objects.get(pk=product_id)

    def create_product(self, data: dict) -> Product:
        return Product.objects.create(**data)

    def update_product(self, product_id: int, data: dict) -> Product:
        product = Product.objects.get(pk=product_id)
        for key, value in data.items():
            setattr(product, key, value)
        product.save()
        return product

    def delete_product(self, product_id: int) -> bool:
       try:
              product = Product.objects.get(pk=product_id)
              product.delete()
              return True
       except Exception as e:
              return False

    def search_products(self, keyword: str) -> List[Product]:
        return Product.objects.filter(name__icontains=keyword)
