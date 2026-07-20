from apscheduler.schedulers.asyncio import AsyncIOScheduler

from database.backups import add_backup

from utils.timezone import now


scheduler = AsyncIOScheduler()



async def create_backup():

    data = {

        "created_at":
            now(),

        "status":
            "completed"
    }


    await add_backup(
        data
    )



def start_backup_scheduler():

    scheduler.add_job(
        create_backup,
        "interval",
        days=1
    )


    scheduler.start()