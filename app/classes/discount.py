from typing import Dict

class Discount:
    """
    Discount - класс для применения скидок.
    """

    discounts : Dict[str, float] = {"season_discount": 10, "promocode_discount": 20}

    @staticmethod
    def calculate_discounted_price(price : float, discount_percent : float) -> float:
        return price * (1 - discount_percent / 100)

    @staticmethod
    def calculate_discounted_price_by_name(price : float, discount_names : list[str]) -> float:
        return price * (1 - Discount.calculate_total_discount(discount_names) / 100)

    @classmethod
    def calculate_total_discount(cls, discount_names : list[str]) -> float:
        return sum(cls.discounts[discount_name] for discount_name in discount_names)

    def __str__(self):
        return f"Класс для применения скидки"