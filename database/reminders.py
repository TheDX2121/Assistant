from database.mongo import db


reminders = db.reminders



async def create_reminder(
    data
):

    await reminders.insert_one(
        data
    )



async def get_pending_reminders():

    result = []


    async for item in reminders.find(
        {
            "status":
                "pending"
        }
    ):

        result.append(
            item
        )


    return result



async def update_reminder(
    reminder_id,
    data
):

    await reminders.update_one(

        {
            "reminder_id":
                reminder_id
        },

        {
            "$set":
                data
        }
    )