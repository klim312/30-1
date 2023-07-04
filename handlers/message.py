import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINs, bot
from sql_tablet.mentors_dp import sql_command_all_ids
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger


async def hello():
    photo = open(r"/Users/klim/Downloads/101021524_0.jpg", "rb")
    for user in ADMINs:
        await bot.send_photo(
            chat_id=user,
            photo=photo,
            caption=f"helooo!!!\n"
                    f"how are you ? "
        )


async def birthday():
    await bot.send_message(
           f"Happy birthday!!"
        )


async def goodbye():
    await bot.send_message(f"goodbye!")


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
          goodbye,
          CronTrigger(hour=00, minute=00, start_date=datetime.datetime.now()), text=f"->")

    scheduler.add_job(hello, IntervalTrigger(seconds=150, start_date=datetime.datetime.now()))

    scheduler.add_job(birthday, DateTrigger(run_date=datetime.datetime(year=2024, month=2, day=21)),)
    scheduler.start()
