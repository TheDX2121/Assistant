from apscheduler.schedulers.asyncio import AsyncIOScheduler

from database.reminders import (
    get_pending_reminders,
    update_reminder
)

from utils.notifier import notify_user


scheduler = AsyncIOScheduler()



async def send_reminders(client):

    reminders = await get_pending_reminders()


    for reminder in reminders:

        try:

            await notify_user(
                client,
                reminder["user_id"],
                reminder["message"]
            )


            await update_reminder(
                reminder["reminder_id"],
                {
                    "status": "sent"
                }
            )


        except Exception:

            pass



def start_reminder_scheduler(
    client
):

    scheduler.add_job(
        send_reminders,
        "interval",
        minutes=1,
        args=[client]
    )

    scheduler.start()