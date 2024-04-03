from dataclasses import dataclass
import uuid



class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.id_s = str(uuid.uuid4())
        self.provider_id = str(uuid.uuid4())

    def __hash__(self):
        return hash((self.id_s, self.provider_id, self.name, self.price))
