class Product:
    """
    Product - класс, представляющий товар.
    """
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Продукт: {self.__name}, цена: {self.__price}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.__name}, {self.__price})"