from database.mongo import db


health = db.health



async def save_health(
    service: str,
    status: str
):

    await health.update_one(
        {
            "service": service
        },

        {
            "$set": {
                "service": service,
                "status": status
            }
        },

        upsert=True
    )



async def get_health():

    result = []

    async for item in health.find():

        result.append(item)

    return result