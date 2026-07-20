from database.mongo import db


cache = db.cache


async def set_cache(
    key: str,
    value,
    expiry=None
):

    data = {
        "key": key,
        "value": value,
        "expiry": expiry
    }

    await cache.update_one(
        {
            "key": key
        },

        {
            "$set": data
        },

        upsert=True
    )


async def get_cache(
    key: str
):

    return await cache.find_one(
        {
            "key": key
        }
    )


async def delete_cache(
    key: str
):

    await cache.delete_one(
        {
            "key": key
        }
    )


async def clear_cache():

    await cache.delete_many({})