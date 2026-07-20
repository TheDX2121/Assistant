from database.mongo import db


users = db.users



async def add_user(
    user_id,
    first_name,
    username
):

    await users.update_one(

        {
            "user_id":
                user_id
        },

        {
            "$set": {

                "user_id":
                    user_id,

                "first_name":
                    first_name,

                "username":
                    username
            }
        },

        upsert=True
    )



async def get_user(
    user_id
):

    return await users.find_one(
        {
            "user_id":
                user_id
        }
    )



async def get_all_users():

    result = []


    async for user in users.find():

        result.append(
            user
        )


    return result