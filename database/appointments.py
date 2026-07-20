from database.mongo import db


appointments = db.appointments



async def create_appointment(
    data
):

    await appointments.insert_one(
        data
    )



async def update_appointment(
    appointment_id,
    data
):

    await appointments.update_one(

        {
            "appointment_id":
                appointment_id
        },

        {
            "$set":
                data
        }
    )



async def get_user_appointments(
    user_id
):

    result = []


    async for item in appointments.find(
        {
            "user_id":
                user_id
        }
    ):

        result.append(
            item
        )


    return result



async def check_time_available(
    date,
    time
):

    found = await appointments.find_one(

        {
            "date":
                date,

            "time":
                time,

            "status":
                {
                    "$in":
                    [
                        "pending",
                        "accepted"
                    ]
                }
        }
    )


    return not bool(found)