from Item import Item
from Store import Store
from Provider import Provider
from Worker import Worker, Courier, Storekeeper
from User import User
from Order import Order

item1 = Item('banana', 50)
item2 = Item('milk', 36)
item3 = Item('orange', 10)
item4 = Item('apple', 39)



store1 = Store('Magnit')
store1.add_item(item1,60)
store1.add_item(item2,10)

provider1 = Provider('Top')
provider1.add_item_provider(item1,100)
provider1.add_item_provider(item2,100)
provider1.add_item_provider(item3,100)

courier1 = Courier(1645654, 'Sasha')

storekeeper1 = Storekeeper(18667876, 'Misha')


User1 = User()



order = User1.make_order()
store1.take_order(order)
store1.set_storekeeper(order)

store1.send_request(item3, provider1, 150)
provider1.update_stocks(item3, store1,100)



print(store1.get_items_store())
print(provider1.get_item_provider())




