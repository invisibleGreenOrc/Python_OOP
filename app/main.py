from classes.order import Order
from classes.customer import Customer
from classes.product import Product
from classes.discount import Discount

# Создаем продукты, заказы, клиентов

product1 = Product("Laptop 1", 1000)
product2 = Product("Laptop 2", 1500)
product3 = Product("Smartphone 1", 500)
product4 = Product("Smartphone 2", 1000)
product5 = Product("SSD 1", 100)
product6 = Product("SSD 2", 200)

order1 = Order([product1])
order2 = Order([product2, product1])
order3 = Order([product3, product4, product5])
order4 = Order([product1, product2, product6])

customer1 = Customer("Иван")
customer2 = Customer("Сергей")

# Добавляем заказы к клиентам

customer1.add_order([order1])
customer2.add_order([order2, order3, order4])


print("Применяем скидки:")
print(f"{product1}, цена со скидкой 15 %: {Discount.calculate_discounted_price(1000, 15)}")
print(f"{product1}, цена со скидкой 'season_discount': {Discount.calculate_discounted_price_by_name(1000, ["season_discount"])}")
print(f"{product1}, цена со скидкой 'season_discount', 'promocode_discount': {Discount.calculate_discounted_price_by_name(1000, ["season_discount", "promocode_discount"])}")

print("\nОбщая информация по всем заказам:")
print(f"Общая сумма всех заказов: {Order.total_orders_price()}")
print(f"Общее количество заказов: {Order.total_orders_count()}")

print("\nИнформация о товарах, заказах, покупателях:")
print(customer1, "\n")
print(customer2, "\n")

# Добавляем скидки в заказы

order1.add_discounts(["season_discount", "promocode_discount"])
order2.add_discounts(["season_discount"])

# Выводим информацию, проверяем, что изменились суммы в заказе, изменилась общая сумма всех заказов всех клиентов

print("После применения скидок\n")
print(customer1, "\n")
print(customer2, "\n")
print(f"Общая сумма всех заказов: {Order.total_orders_price()}\n")

# Проверяем, как работает сравнение продуктов 

print(product1 < product2)
print(product1 == product2)
print(product1 > product2)

print(repr(customer1))