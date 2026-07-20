from database.mongo import db


blacklist = db.blacklist



async def add_blacklist(
    user_id: int,
    reason: str = None
):

    await blacklist.update_one(
        {
            "user_id": user_id
        },

        {
            "$set": {
                "user_id": user_id,
                "reason": reason
            }
        },

        upsert=True
    )



async def is_blacklisted(
    user_id: int
):

    user = await blacklist.find_one(
        {
            "user_id": user_id
        }
    )

    return bool(user)



async def remove_blacklist(
    user_id: int
):

    await blacklist.delete_one(
        {
            "user_id": user_id
        }
    )