from apscheduler.schedulers.asyncio import AsyncIOScheduler

from database.cache import clear_cache


scheduler = AsyncIOScheduler()



async def cleanup():

    await clear_cache()



def start_cleanup():

    scheduler.add_job(
        cleanup,
        "interval",
        hours=24
    )

    scheduler.start()