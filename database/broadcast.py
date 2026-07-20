from database.mongo import db


broadcasts = db.broadcasts



async def create_broadcast(
    data: dict
):

    await broadcasts.insert_one(
        data
    )



async def update_broadcast(
    broadcast_id: str,
    data: dict
):

    await broadcasts.update_one(
        {
            "broadcast_id": broadcast_id
        },

        {
            "$set": data
        }
    )



async def get_broadcasts():

    result = []

    async for item in broadcasts.find():

        result.append(item)

    return result