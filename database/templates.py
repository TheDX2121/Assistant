from database.mongo import db


templates = db.templates



async def save_template(
    name: str,
    text: str
):

    await templates.update_one(
        {
            "name": name
        },

        {
            "$set": {
                "name": name,
                "text": text
            }
        },

        upsert=True
    )



async def get_template(
    name: str
):

    return await templates.find_one(
        {
            "name": name
        }
    )



async def get_all_templates():

    result = []

    async for item in templates.find():

        result.append(item)

    return result