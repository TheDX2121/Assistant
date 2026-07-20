from database.mongo import db


tickets = db.tickets



async def create_ticket(
    data
):

    await tickets.insert_one(
        data
    )



async def add_message(
    ticket_id,
    message
):

    await tickets.update_one(

        {
            "ticket_id":
                ticket_id
        },

        {
            "$push":
            {
                "messages":
                    message
            }
        }
    )



async def get_ticket(
    ticket_id
):

    return await tickets.find_one(

        {
            "ticket_id":
                ticket_id
        }
    )