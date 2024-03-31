from dataclasses import dataclass


@dataclass
class Item:
    id_s: int
    provider_id: int
    name: str
    price: float

    def __hash__(self):
        return hash((self.id_s, self.provider_id, self.name, self.price))
