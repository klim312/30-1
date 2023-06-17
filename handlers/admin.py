from aiogram import types, Dispatcher
from config import bot, ADMINs
import random


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINs:
            await message.answer("вы не обладаете правами Администратора!!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await message.delete()
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(
                f"{message.from_user.first_name} братан, кикнул "
                f"{message.reply_to_message.from_user.full_name}"
            )
    else:
        await message.answer("Пиши в группе!")


async def pin(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINs:
            await message.answer("вы не обладаете правами Администратора!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await message.delete()
            await bot.pin_chat_message(
                message.chat.id,
                message.reply_to_message.message_id
            )
            await message.answer(
                f"{message.from_user.first_name} успешно закреплено! "
                f"{message.reply_to_message.from_user.full_name}"
            )
    else:
        await message.answer("Пишите в группе!")


async def game(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer("вы не обладаете правами Администратора!")
    else:
        await message.answer_dice(random.choices(emoji_game))
        await message.answer(f"добро пожаловать! {message.from_user.full_name}")

a = "\U0001F3B2"  # 🎲
b = "\U0001F3AF"  # 🎯
c = "\U0001F3B0"  # 🎰
d = "\U0001F3B3"  # 🎳
e = "\U000026BD"  # ⚽
f = "\U0001F3C0"  # 🏀
emoji_game = [a, b, c, d, e, f]


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(game, text=['game'])
