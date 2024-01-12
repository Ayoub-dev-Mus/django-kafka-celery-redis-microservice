from typing import List, Optional
from ..repository import CartRepository
from .cartService import CartService
from ..models import Cart

class CartServiceImpl(CartService):
    def __init__(self):
        super().__init__(CartRepository())

    def find_all_carts(self) -> List[Cart]:
        return CartRepository().find_all_carts()

    def find_cart_by_user_id(self, user_id: int) -> Optional[Cart]:
        return CartRepository().find_cart_by_user_id(user_id)

    def add_product_to_cart(self, cart_data: dict) -> Cart:
        return CartRepository().add_product_to_cart(cart_data)

    def update_cart(self, user_id: int, cart_data: dict) -> Optional[Cart]:
        return CartRepository().update_cart(user_id, cart_data)

    def remove_product_from_cart(self, user_id: int, product_id: int) -> Optional[Cart]:
        return CartRepository().remove_product_from_cart(user_id, product_id)

    def clear_cart(self, user_id: int) -> bool:
        return CartRepository().clear_cart(user_id)
