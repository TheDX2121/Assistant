from database.mongo import db


tickets = db.tickets


async def create_ticket(
    data: dict
):

    await tickets.insert_one(data)


async def get_ticket(
    ticket_id: str
):

    return await tickets.find_one(
        {
            "ticket_id": ticket_id
        }
    )


async def update_ticket(
    ticket_id: str,
    data: dict
):

    await tickets.update_one(
        {
            "ticket_id": ticket_id
        },

        {
            "$set": data
        }
    )


async def add_message(
    ticket_id: str,
    message: dict
):

    await tickets.update_one(
        {
            "ticket_id": ticket_id
        },

        {
            "$push": {
                "messages": message
            },

            "$set": {
                "last_message":
                    message
            }
        }
    )


async def get_user_tickets(
    user_id: int
):

    result = []

    async for ticket in tickets.find(
        {
            "user_id": user_id
        }
    ):

        result.append(ticket)


    return result