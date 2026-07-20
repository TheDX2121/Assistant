from database.mongo import db


payments = db.payments



async def create_payment(
    data: dict
):

    await payments.insert_one(
        data
    )



async def get_payment(
    payment_id: str
):

    return await payments.find_one(
        {
            "payment_id": payment_id
        }
    )



async def update_payment(
    payment_id: str,
    data: dict
):

    await payments.update_one(
        {
            "payment_id": payment_id
        },

        {
            "$set": data
        }
    )



async def get_user_payments(
    user_id: int
):

    result = []

    async for item in payments.find(
        {
            "user_id": user_id
        }
    ):

        result.append(item)


    return result