from Order import Order


class Store:
    def __init__(self, id_s, name, coordinates):
        self.__id_s = id_s
        self.__name = name
        self.__coordinates = coordinates
        self.__items_store = {}

    def get_id_s(self):
        return self.__id_s

    def set_id_s(self, id_s):
        self.__id_s = id_s

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_coordinates(self):
        return self.__coordinates

    def set_coordinates(self, coordinates):
        self.__coordinates = coordinates

    def get_items_store(self):
        return self.__items_store

    def set_items_store(self, items_store):
        self.__items_store = items_store

    def add_item(self, item, count):
        self.__items_store[item] = count

    def send_request(self, item, provider, count):
        if item not in self.__items_store:
            print(f"Запрашиваем товар {item.name} у поставщика в кол-ве {count}")
            provider.send_order(item, count)

    def take_order(self, order):
        order.status = "processing"
        print(f"Статус заказа: {order.status}")

    def set_storekeeper(self):
        pass

    def set_courier(self):
        pass

    def get_worker(self):
        pass
