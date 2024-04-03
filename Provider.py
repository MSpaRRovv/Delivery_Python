import uuid
class Provider:
    def __init__(self, name):
        self.id_p =  str(uuid.uuid4())
        self.name = name
        self.items_provider = {}



    def add_item_provider(self, item, count):
        self.items_provider[item] = count

    def get_item_provider(self):
        return self.items_provider

    def send_order(self, item, count):
        if item in self.items_provider:
            available_quantity = self.items_provider[item]
            if available_quantity >= count:
                print(f"Отправлен заказ на {count} единиц товара {item.name} магазину")
                self.items_provider[item] -= count
                return count
            else:
                print(f"Отправлен заказ на {available_quantity} единиц товара {item.name} (максимальное количество) магазину")
                self.items_provider[item] = 0  # Заказываем максимально доступное количество
                return available_quantity  # Возвращаем максимально доступное количество
        else:
            print("Товар не доступен")



    def update_stocks(self, item, store, count):
        store.add_item(item, count)
        print(f"Обновлено количество товара {item.name} в магазине")



