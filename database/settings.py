from database.mongo import db


settings = db.settings


async def get_settings():

    data = await settings.find_one(
        {
            "_id": "bot_settings"
        }
    )


    if data:
        return data


    default = {

        "_id": "bot_settings",

        "timezone":
            "Asia/Kolkata",

        "meeting_start":
            "13:00",

        "meeting_end":
            "23:00",

        "meeting_duration":
            30,

        "reminder_interval":
            15,

        "maintenance_mode":
            False,

        "sandbox_mode":
            False
    }


    await settings.insert_one(
        default
    )

    return default



async def update_settings(
    data: dict
):

    await settings.update_one(

        {
            "_id":
            "bot_settings"
        },

        {
            "$set": data
        },

        upsert=True
    )