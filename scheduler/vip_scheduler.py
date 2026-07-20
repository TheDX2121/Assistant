from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from database.vip import vip_collection


scheduler = AsyncIOScheduler()



async def check_vip_expiry():

    current = datetime.now()


    await vip_collection.update_many(

        {
            "expiry": {
                "$lt": current
            },

            "status": "active"
        },

        {
            "$set": {
                "status": "expired"
            }
        }
    )



def start_vip_scheduler():

    scheduler.add_job(
        check_vip_expiry,
        "interval",
        hours=1
    )


    scheduler.start()