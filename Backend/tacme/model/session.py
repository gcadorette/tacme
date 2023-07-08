from dataclasses import dataclass
import datetime

@dataclass
class Session:
    hash: str
    created_at: datetime