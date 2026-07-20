from database.mongo import db



async def search_user(
    query
):

    return await db.users.find_one(
        {
            "$or": [
                {
                    "username":
                    query
                },

                {
                    "user_id":
                    query
                }
            ]
        }
    )



async def search_appointment(
    appointment_id
):

    return await db.appointments.find_one(
        {
            "appointment_id":
            appointment_id
        }
    )



async def search_ticket(
    ticket_id
):

    return await db.tickets.find_one(
        {
            "ticket_id":
            ticket_id
        }
    )