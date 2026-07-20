from database.mongo import db


statistics = db.statistics


async def get_statistics():

    data = await statistics.find_one(
        {
            "_id": "stats"
        }
    )

    if data:
        return data


    default = {
        "_id": "stats",

        "total_users": 0,

        "total_appointments": 0,
        "accepted_appointments": 0,
        "rejected_appointments": 0,
        "completed_appointments": 0,

        "total_emergencies": 0,

        "total_tickets": 0,

        "vip_members": 0,

        "trusted_users": 0
    }


    await statistics.insert_one(default)

    return default



async def update_stat(
    field: str,
    value: int = 1
):

    await statistics.update_one(
        {
            "_id": "stats"
        },

        {
            "$inc": {
                field: value
            }
        },

        upsert=True
    )