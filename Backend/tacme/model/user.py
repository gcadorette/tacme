from dataclasses import dataclass, field
from tacme.model.role import Role

@dataclass
class User:
    user_name: str
    hash_str: str
    roles: list[Role] = field(default_factory=list)