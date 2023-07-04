from aiogram import executor
import logging
from config import dp, bot, ADMINs
from handlers import commands, callback, extra, dice, admin, fsm_mentor, mentor_admin, message
from sql_tablet.mentors_dp import sql_create
from x_new import new_functional


commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
extra.register_handlers_extra(dp)
dice.register_handlers_1commands(dp)
fsm_mentor.register_handlers_commands(dp)
mentor_admin.register_handlers_admin(dp)
new_functional.register_handlers_2commands(dp)


async def on_startup(dp):
    sql_create()

    await bot.send_message(ADMINs[0], f"I'm here")
    await message.set_scheduler()


async def on_shutdown(dp):
    await bot.send_message(ADMINs[0], "Bye!")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
