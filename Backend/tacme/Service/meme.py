from tacme.model.file_format import FileFormat
from tacme.model.meme import Meme
from tacme.client.mongo import get_memes_collection

def get_all_memes():
    memes = get_memes_collection().find()
    memesDto = []
    for meme in memes:
        memesDto.append(Meme(FileFormat(meme['format']), meme['link']))
    return memesDto