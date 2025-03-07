from classes.product import Product

class Order:
    """
    Order - класс, представляющий заказ.
    """
    _orders = []

    def __init__(self, products: list[Product]):
        self.__products = products
        Order._orders.append(self)

    @classmethod
    def total_orders_count(cls) -> int:
        return len(cls._orders)
    
    @classmethod
    def total_orders_price(cls) -> float:
        return sum([order.get_price() for order in cls._orders])

    def get_price(self) -> float:
        return sum([product.price for product in self.__products])
    
    def __str__(self):
        return f"Заказ с продуктами:\n{'\n'.join(f"- {product}" for product in self.__products)}\nЦена заказа: {self.get_price()}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__products})"