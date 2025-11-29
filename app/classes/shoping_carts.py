# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self, customer):
        self.items = []
        self.customer = customer
        self.salesperson = None
        self.is_paid = False

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"Продукт": product, "количество": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["Продукт"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["Продукт"].price * item["количество"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details = "Корзина покупок:\n"
        details += f"{self.customer.get_details()}\n"

        for item in self.items:
            details += f"{item['Продукт'].get_details()}, Количество: {item['количество']}\n"
        details += f"Общее: {self.get_total()} руб"

        if self.is_paid:
            details += "\nВсе покупки оплачены."
            if self.salesperson is not None:
                details += f"\nПродавец: {self.salesperson.get_details()}"

        return details
    
    def confirm_payment(self, salesperson):
        """
        Подтверждает оплату всех товаров корзины.
        """
        self.is_paid = True
        self.salesperson = salesperson