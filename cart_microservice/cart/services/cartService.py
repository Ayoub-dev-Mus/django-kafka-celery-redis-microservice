from abc import ABC, abstractmethod
from typing import List, Optional
from ..repository import CartRepository
from ..models import Cart

class CartService(ABC):
    def __init__(self, repository: CartRepository):
        self.repository = repository

    @abstractmethod
    def find_all_carts(self) -> List[Cart]:
        return self.repository.find_all_carts()

    @abstractmethod
    def find_cart_by_user_id(self, user_id: int) -> Optional[Cart]:
        return self.repository.find_cart_by_user_id(user_id)

    @abstractmethod
    def add_product_to_cart(self, cart_data: dict) -> Cart:
        return self.repository.add_product_to_cart(cart_data)

    @abstractmethod
    def update_cart(self, user_id: int, cart_data: dict) -> Optional[Cart]:
        return self.repository.update_cart(user_id, cart_data)

    @abstractmethod
    def remove_product_from_cart(self, user_id: int, product_id: int) -> Optional[Cart]:
        return self.repository.remove_product_from_cart(user_id, product_id)

    @abstractmethod
    def clear_cart(self, user_id: int) -> bool:
        return self.repository.clear_cart(user_id)
