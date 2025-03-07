from classes.order import Order
from classes.customer import Customer
from classes.product import Product

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

customer1.add_order([order1])
customer2.add_order([order2, order3, order4])

print(order1)
print(order2)
print(order3)
print(order4)

print(f"\nОбщая сумма всех заказов: {Order.total_orders_price()}")
print(f"\nОбщее количество заказов: {Order.total_orders_count()}")



print(customer2)