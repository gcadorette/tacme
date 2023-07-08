from dataclasses import dataclass

from tacme.model.file_format import FileFormat

@dataclass
class Meme:
    format: FileFormat
    link: str
