from database.mongo import db


logs = db.logs



async def add_log(
    data
):

    await logs.insert_one(
        data
    )



async def get_logs(
    limit=20
):

    result = []


    async for item in logs.find().sort(
        "_id",
        -1
    ).limit(limit):

        result.append(
            item
        )


    return result