from database.mongo import db


appointments = db.appointments


async def create_appointment(
    data: dict
):

    await appointments.insert_one(
        data
    )


async def get_appointment(
    appointment_id: str
):

    return await appointments.find_one(
        {
            "appointment_id":
                appointment_id
        }
    )


async def update_appointment(
    appointment_id: str,
    data: dict
):

    await appointments.update_one(
        {
            "appointment_id":
                appointment_id
        },

        {
            "$set": data
        }
    )


async def check_time_available(
    date,
    time
):

    existing = await appointments.find_one(
        {
            "date": date,
            "time": time,

            "status": {
                "$in": [
                    "pending",
                    "accepted"
                ]
            }
        }
    )


    if existing:
        return False


    return True


async def get_user_appointments(
    user_id: int
):

    result = []

    async for item in appointments.find(
        {
            "user_id": user_id
        }
    ):

        result.append(item)


    return result