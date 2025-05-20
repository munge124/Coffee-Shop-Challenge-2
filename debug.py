from customer import Customer
from coffee import Coffee


alice = Customer("Alice")
latte = Coffee("Latte")

order = alice.create_order(latte, 5.5)


print("Customer:", alice.name)
print("Coffee:", latte.name)
print("Orders:", alice.orders())
print("Coffees ordered by Alice:", [c.name for c in alice.coffees()])
print("Latte num_orders:", latte.num_orders())
print("Latte average price:", latte.average_price())
