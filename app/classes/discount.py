class Discount:
    """
    Discount - класс для применения скидок.
    """
    def __init__(self, description: str, discount_percent: float):
        self.__description = description
        self.__discount_percent = discount_percent

    def __str__(self):
        return f"Класс для применения скидки"