from classes.order import Order

class Customer:
    """
    Customer - класс, представляющий клиента.
    """
    def __init__(self, name: str):
        self.__name = name
        self.__orders : list[Order]

    def __str__(self):
        return f"Клиент: {self.__name}, заказы:\n{self.__orders})"