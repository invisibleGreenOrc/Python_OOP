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

print(order1.get_price())
print(order2.get_price())

print(Order.total_orders_price())
print(Order.total_orders_count())