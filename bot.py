from pyrogram import Client

from config import config

from plugins.register import load_plugins

from scheduler.task_manager import (
    start_all_tasks
)

from utils.startup import (
    startup_message
)



app = Client(

    "PersonalAssistant",

    api_id=config.API_ID,

    api_hash=config.API_HASH,

    bot_token=config.BOT_TOKEN

)



load_plugins(
    app
)



@app.on_message()
async def startup(
    client,
    message
):

    pass



async def main():

    await app.start()


    start_all_tasks(
        app
    )


    print(
        await startup_message()
    )


    await idle()



if __name__ == "__main__":

    app.run()