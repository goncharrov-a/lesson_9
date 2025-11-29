from dataclasses import dataclass


@dataclass
class SimpleUser:
    full_name: str
    email: str
    current_address: str
    permanent_address: str
