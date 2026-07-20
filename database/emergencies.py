from database.mongo import db


emergencies = db.emergencies


async def create_emergency(data: dict):
    """
    Create a new emergency request.
    """

    await emergencies.insert_one(data)


async def get_emergency(
    emergency_id: str
):

    return await emergencies.find_one(
        {
            "emergency_id": emergency_id
        }
    )


async def update_emergency(
    emergency_id: str,
    data: dict
):

    await emergencies.update_one(
        {
            "emergency_id": emergency_id
        },

        {
            "$set": data
        }
    )


async def get_user_emergencies(
    user_id: int
):

    result = []

    async for item in emergencies.find(
        {
            "user_id": user_id
        }
    ):

        result.append(item)

    return result