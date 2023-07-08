from dataclasses import dataclass, field
import datetime

from tacme.model.file_format import FileFormat

@dataclass
class Meme:
    format: FileFormat
    link: str
    created_at: datetime
    title: str
    tags: list[str] = field(default_factory=list)
