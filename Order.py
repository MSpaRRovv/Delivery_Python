from dataclasses import dataclass
import uuid
from typing import Dict, List, Tuple
from Item import Item


@dataclass
class Order:

    order_id: int
    status: str
    items: Dict[Item, int]
    created_at: str
    delivered_at: str
    assembler: str
    delivery_person: str
