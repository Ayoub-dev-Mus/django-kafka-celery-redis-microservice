from .models import Cart
from typing import List

class CartRepository:
    def find_all_carts(self) -> List[Cart]:
        return Cart.objects.all()

    def find_cart_by_user_id(self, user_id: int) -> Cart:
        return Cart.objects.get(user_id=user_id)

    def add_product_to_cart(self,data: dict) -> Cart:
         return Cart.objects.create(**data)


    def update_cart(self, user_id: int, data: dict) -> Cart:
        cart = Cart.objects.get(user_id=user_id)
        for key, value in data.items():
            setattr(cart, key, value)
        cart.save()
        return cart

    def remove_product_from_cart(self, user_id: int, product_id: int) -> Cart:
        cart = Cart.objects.get(user_id=user_id)
        cart.products.remove(product_id)
        return cart

    def clear_cart(self, user_id: int) -> bool:
        try:
            cart = Cart.objects.get(user_id=user_id)
            cart.products.clear()
            cart.quantity = 0
            cart.save()
            return True
        except Cart.DoesNotExist:
            return False
