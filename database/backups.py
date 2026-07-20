from database.mongo import db


backups = db.backups



async def add_backup(
    data: dict
):

    await backups.insert_one(
        data
    )



async def get_backups():

    result = []

    async for backup in backups.find().sort(
        "created_at",
        -1
    ):

        result.append(backup)

    return result



async def delete_backup(
    backup_id: str
):

    await backups.delete_one(
        {
            "backup_id": backup_id
        }
    )