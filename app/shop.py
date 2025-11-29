from classes.products import Electronics, Clothing, Household_Chemicals
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart


# Создаем продукты
laptop = Electronics(name="Ноутбук", price=120000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
soap = Household_Chemicals(name="Мыло для рук", price=50, form="Жидкость", scent="Лимон")

# Создаем пользователей
customer = Customer(username="Mikhail", email="python@derkunov.ru", address="033 Russ Bur")
admin = Admin(username="root", email="root@derkunov.ru", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(customer)
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)

# Выводим детали корзины
print(cart.get_details())

cart.confirm_payment(None)
print(cart.get_details())


cart = ShoppingCart(customer)
cart.add_item(tshirt, 2)
cart.add_item(soap, 1)

# Выводим детали корзины
print(cart.get_details())

cart.confirm_payment(admin)
print(cart.get_details())