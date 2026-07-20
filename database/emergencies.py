from database.mongo import db


emergencies = db.emergencies



async def create_emergency(
    data
):

    await emergencies.insert_one(
        data
    )



async def update_emergency(
    emergency_id,
    data
):

    await emergencies.update_one(

        {
            "emergency_id":
                emergency_id
        },

        {
            "$set":
                data
        }
    )



async def get_emergencies():

    result = []


    async for item in emergencies.find():

        result.append(
            item
        )


    return result