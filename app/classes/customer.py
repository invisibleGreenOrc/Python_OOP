from classes.order import Order

class Customer:
    """
    Customer - класс, представляющий клиента.
    """
    def __init__(self, name: str):
        self.__name = name
        self.__orders = list[Order]()

    def add_order(self, order : list[Order]):
        self.__orders.extend(order)

    def __str__(self):
        return f"Клиент: {self.__name}, заказы:\n{'\n'.join(f" {order}" for order in self.__orders)}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.__orders})"