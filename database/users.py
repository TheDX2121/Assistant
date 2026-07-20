from database.mongo import db


users = db.users


async def add_user(
    user_id: int,
    first_name: str,
    username: str = None
):

    data = {
        "user_id": user_id,
        "first_name": first_name,
        "username": username,

        "profile_link":
            f"tg://user?id={user_id}",

        "trusted": False,

        "vip": False,
        "vip_expiry": None,

        "blacklisted": False,

        "total_appointments": 0,
        "total_tickets": 0,
        "total_emergencies": 0,

        "created_at": None,
        "updated_at": None
    }


    await users.update_one(
        {
            "user_id": user_id
        },

        {
            "$setOnInsert": data
        },

        upsert=True
    )


async def get_user(
    user_id: int
):

    return await users.find_one(
        {
            "user_id": user_id
        }
    )


async def update_user(
    user_id: int,
    data: dict
):

    await users.update_one(
        {
            "user_id": user_id
        },

        {
            "$set": data
        }
    )


async def get_all_users():

    result = []

    async for user in users.find():

        result.append(user)

    return result