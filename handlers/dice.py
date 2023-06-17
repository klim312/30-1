from aiogram import types, Dispatcher
from config import bot


async def bot_dice(message: types.Message):

        await bot.send_message(message.chat.id, f"запуск {message.from_user.full_name}\n"
                                                f"первый кидает бот --> ")

        bot1 = await message.answer_dice()
        print(bot1)

        await bot.send_message(message.chat.id, f"балл : {bot1.dice.value}\n"
                                                f"ваша очередь  --> \n")

        await bot.send_message(message.chat.id, f" {message.from_user.full_name}\n"
                                                f"ваш ход--> ")

        user = await message.answer_dice()
        print(user)

        await bot.send_message(message.chat.id, f"балл : {user.dice.value}\n"
                                                f"итог --> \n")

        if bot1.dice.value == user.dice.value:
            await bot.send_message(message.chat.id, "ничья")

        elif bot1.dice.value < user.dice.value:
            await bot.send_message(message.chat.id, f"победитель -> {message.from_user.full_name}")

        elif bot1.dice.value > user.dice.value:
            await bot.send_message(message.chat.id, f"победитель -> BOT")
        else:
            await bot.send_message(message.chat.id, f"победитель -> BOT")


def register_handlers_1commands(dp: Dispatcher):
    dp.register_message_handler(bot_dice,commands=['dice'])
