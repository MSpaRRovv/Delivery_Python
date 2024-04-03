from Item import Item
from Store import Store
from Provider import Provider
from Worker import Worker, Courier, Storekeeper
from User import User
from Order import Order

item1 = Item(1, 1144234, 'banana', 50)
item2 = Item(2, 234534, 'milk', 36)
item3 = Item(3, 345345, 'orange', 10)
item4 = Item(4, 453453, 'apple', 39)

store1 = Store(25, 'Magnit', (10, 10))
store1.add_item(item1,60)
store1.add_item(item2,10)

provider1 = Provider(1, 'Magnit')
provider1.add_item_provider(item1,100)
provider1.add_item_provider(item2,100)
provider1.add_item_provider(item3,100)

courier1 = Courier(1645654, 'Sasha')

storekeeper1 = Storekeeper(18667876, 'Misha')

User1 = User('Andrew', 123456789, (24,24))
order = User1.make_order()
store1.take_order(order)

store1.send_request(item3, provider1, 150)
provider1.update_stocks(item3, store1,100)



print(store1.get_items_store())
print(provider1.get_item_provider())



