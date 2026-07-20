from database.mongo import db


trusted_users = db.trusted_users


async def add_trusted(
    data: dict
):

    await trusted_users.insert_one(
        data
    )


async def get_trusted(
    user_id: int
):

    return await trusted_users.find_one(
        {
            "user_id": user_id
        }
    )


async def remove_trusted(
    user_id: int
):

    await trusted_users.delete_one(
        {
            "user_id": user_id
        }
    )


async def get_all_trusted():

    result = []

    async for user in trusted_users.find():

        result.append(user)

    return result