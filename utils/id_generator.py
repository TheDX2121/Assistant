from database.mongo import db



async def generate_id(
    collection,
    prefix
):

    count = await db[collection].count_documents({})

    number = count + 1

    return (
        f"{prefix}-"
        f"{number:06d}"
    )