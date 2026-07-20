from database.mongo import db


vip_collection = db.vip


async def create_vip(
    data: dict
):

    await vip_collection.insert_one(
        data
    )


async def get_vip(
    user_id: int
):

    return await vip_collection.find_one(
        {
            "user_id": user_id,
            "status": "active"
        }
    )


async def update_vip(
    user_id: int,
    data: dict
):

    await vip_collection.update_one(
        {
            "user_id": user_id
        },

        {
            "$set": data
        }
    )


async def remove_vip(
    user_id: int
):

    await vip_collection.update_one(
        {
            "user_id": user_id
        },

        {
            "$set": {
                "status": "expired"
            }
        }
    )


async def get_all_vips():

    result = []

    async for item in vip_collection.find():

        result.append(item)

    return result