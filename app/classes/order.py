from classes.product import Product
from classes.discount import Discount

class Order:
    """
    Order - класс, представляющий заказ.
    """
    _orders : list["Order"] = []

    def __init__(self, products: list[Product]):
        self.__products = products
        self.__applied_discounts : list[str] = []
        Order._orders.append(self)

    @classmethod
    def total_orders_count(cls) -> int:
        return len(cls._orders)
    
    @classmethod
    def total_orders_price(cls) -> float:
        return sum([order.get_price() for order in cls._orders])

    def get_price(self, apply_discounts : bool = True) -> float:
        price = sum([product.price for product in self.__products])

        if apply_discounts:
            return Discount.calculate_discounted_price_by_name(price, self.__applied_discounts)

        return price
    
    def add_discounts(self, discounts_names : list[str]):
        self.__applied_discounts.extend(discounts_names)
    
    def __str__(self):
        description = f"Заказ с продуктами:\n{'\n'.join(f"- {product}" for product in self.__products)}\nЦена заказа: {self.get_price()}"
        if len(self.__applied_discounts) > 0:
            description = f"Заказ с продуктами:\n{'\n'.join(f"- {product}, цена со скидкой: {Discount.calculate_discounted_price_by_name(product.price, self.__applied_discounts)}" for product in self.__products)}\nЦена заказа: {self.get_price(apply_discounts = False)}, цена заказа со скидкой: {self.get_price()}"
        return description
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__products}, {self.__applied_discounts})"