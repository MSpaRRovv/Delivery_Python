from dataclasses import dataclass


@dataclass
class Order:
    order_id: int
    status: str
    items: list
    created_at: str
    delivered_at: str
    assembler: str
    delivery_person: str
