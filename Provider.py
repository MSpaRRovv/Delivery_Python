class Provider:
    def __init__(self, id_p, name):
        self.id_p = id_p
        self.name = name
        self.items_provider = {}

    def add_item_provider(self, item, count):
        self.items_provider[item] = count

    def get_item_provider(self):
        return self.items_provider

    def send_order(self, item, count):
        if item in self.items_provider:
            possible_quantity = self.items_provider[item]
            if possible_quantity >= count:
                print(f"Отправлен заказ на {count} едениц товара {item.name} магазину")
            else:
                print(f"Отправлен заказ на {possible_quantity} едениц товара {item.name} (максимальное количество) магазину")
        else:
            print("Товар не доступен")

    def update_stocks(self, item, count):
        if item in self.items_provider:
            if count <= 0:
                print("Ошибка: Количество должно быть больше нуля.")
                return 0
            if count > self.items_provider[item]:
                count = self.items_provider[item]
            self.items_provider[item] -= count
            print(f"Обновлено количество товара {item.name} у поставщика. Текущее количество: {self.items_provider[item]}")
            return count
        else:
            print("Товар не найден у поставщика.")
            return 0
