from Item import Item
from Store import Store

item1 = Item(1, 1144234, 'banana', 50)
item2 = Item(2, 234534, 'milk', 36)

store1 = Store(25, 'Magnit', (10, 10))

store1.add_item(item1,50)
store1.add_item(item2,100)

print(store1.get_items_store())



