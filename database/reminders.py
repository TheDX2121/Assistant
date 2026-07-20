from database.mongo import db


reminders = db.reminders


async def create_reminder(
    data: dict
):

    await reminders.insert_one(
        data
    )


async def get_pending_reminders():

    result = []

    async for reminder in reminders.find(
        {
            "status": "pending"
        }
    ):

        result.append(reminder)

    return result


async def update_reminder(
    reminder_id: str,
    data: dict
):

    await reminders.update_one(
        {
            "reminder_id": reminder_id
        },

        {
            "$set": data
        }
    )


async def delete_reminder(
    reminder_id: str
):

    await reminders.delete_one(
        {
            "reminder_id": reminder_id
        }
    )