from dataclasses import dataclass
from tacme.model.meme import Meme

@dataclass
class AddFileRequest:
    user_hash: str
    meme: Meme