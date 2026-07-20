from database.mongo import db


logs = db.logs



async def add_log(
    data: dict
):

    await logs.insert_one(
        data
    )



async def get_logs(
    limit: int = 50
):

    result = []

    async for log in logs.find().sort(
        "time",
        -1
    ).limit(limit):

        result.append(log)


    return result



async def clear_logs():

    await logs.delete_many({})