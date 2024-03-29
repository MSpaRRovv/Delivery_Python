class Item:
    def __init__(self, id_s, provider_id, name, price):
        self.id_s = id_s
        self.provider_id = provider_id
        self.name = name
        self.price = price


class Provider:
    def __init__(self, id_p, name):
        self.id_p = id_p
        self.name = name
        self.items_provider = {}

    def add_item_provider(self, item, count):
        key = item.provider_id
        if key in self.items_provider:
            self.items_provider[key] += count
        else:
            self.items_provider[key] = count

    def send_order(self, item_n):
        if item_n.provider_id in self.items_provider:
            print("Otpravlen")

    def update_stocks_provider(self, items_n):
        add_item_provider = items_n.add_item_provider
        del self.items_provider[items_n.provider_id]





class Store:
    def __init__(self, name, store_id):
        self.name = name
        self.store_id = store_id
        self.items_store = {}

    def add_item_store(self, item, count):
        key = item.id_s
        if key in self.items_store:
            self.items_store[key] += count
        else:
            self.items_store[key] = count

    def send_request(self, order):
        if order not in self.items_store:
            print(f"Order not found, please we need {order.name} items")

    def update_stocks_store(self, item_n):
        print("nice")




