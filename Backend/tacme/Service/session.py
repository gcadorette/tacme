import datetime
from tacme.client.mongo import get_sessions_collection
from tacme.model.session import Session
from tacme.service.date import get_datetime
from tacme.service.crypto import generate_hash
import random
import string

EXPIRATION = 2 * 60 * 60 # 2 hours in seconds
SESSION_HASH_LENGTH = 20

def is_valid(session_hash: str):
    session_entry = get_sessions_collection().find_one({"session_hash": session_hash})
    if session_entry is None:
        return False
    session = Session(session_entry["session_hash"], session_entry["created_at"].isoformat())

    diff = (datetime.today() - session.created_at).seconds()
    if diff < EXPIRATION:
        return False
    return True

def create_session():
    randomStr = ''.join(random.choice(string.ascii_letters) for i in range(SESSION_HASH_LENGTH))
    randomStr += get_datetime()
    hashedStr = generate_hash(randomStr)

    session_collection = get_sessions_collection()
    session_collection.insert_one({
        "hash": hashedStr,
        "created_at": get_datetime()
    })
    return hashedStr
