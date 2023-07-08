from tacme.model.file_format import FileFormat
from tacme.model.meme import Meme
from tacme.client.mongo import get_memes_collection
from tacme.service.date import get_datetime

def get_all_memes():
    memes = get_memes_collection().find()
    memesDto = []
    for meme in memes:
        print(meme)
        # memesDto.append(Meme(FileFormat(meme['format']), meme['link']))
    return memesDto

def get_all_tags():
    tags = get_memes_collection().find({}, {"tags": 1})
    alltags = []
    for tag in tags:
        if tag not in alltags:
            alltags.append(tag)
    return alltags

def add_meme(meme: Meme):
    collection = get_memes_collection()
    element = {
        "format": int(meme.format),
        "link": meme.link,
        "tags": meme.tags,
        "title": meme.title,
        "created_at": get_datetime()
    }
    inserted = collection.insert_one(element)
    return inserted.inserted_id