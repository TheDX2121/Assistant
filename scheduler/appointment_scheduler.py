from apscheduler.schedulers.asyncio import AsyncIOScheduler

from database.appointments import appointments
from utils.timezone import now
from utils.notifier import notify_owner


scheduler = AsyncIOScheduler()



async def check_appointments(
    client
):

    current_time = now()


    async for appointment in appointments.find(
        {
            "status": "accepted"
        }
    ):

        meeting_time = appointment.get(
            "time"
        )


        # Reminder checking will be connected
        # with appointment date/time system


        if meeting_time:

            pass



def start_scheduler(
):

    scheduler.add_job(
        check_appointments,
        "interval",
        minutes=1
    )


    scheduler.start()