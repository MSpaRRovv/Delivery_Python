from Classes import Item, Provider, Store

item1 = Item(1, 1144234, 'banana', 50)
item2 = Item(2, 234534, 'milk', 36)

provider1 = Provider(1, 'Saha')

provider1.add_item_provider(item1, 50)
provider1.add_item_provider(item2, 20)

store1 = Store('Magnit', 4242)

store1.add_item_store(item1, 2)
store1.send_request(item2)
provider1.send_order(item2)
provider1.update_stocks_provider(item2)

print(provider1.items_provider)


