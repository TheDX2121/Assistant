from database.users import get_all_users



async def broadcast(
    client,
    message
):

    users = await get_all_users()


    success = 0
    failed = 0


    for user in users:

        try:

            await client.send_message(
                user["user_id"],
                message
            )

            success += 1


        except Exception:

            failed += 1


    return {
        "success": success,
        "failed": failed
    }