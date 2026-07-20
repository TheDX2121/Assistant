from database.mongo import db


timeline = db.timeline



async def add_event(
    data: dict
):

    await timeline.insert_one(
        data
    )



async def get_user_timeline(
    user_id: int
):

    result = []

    async for event in timeline.find(
        {
            "user_id": user_id
        }
    ).sort(
        "created_at",
        -1
    ):

        result.append(event)


    return result