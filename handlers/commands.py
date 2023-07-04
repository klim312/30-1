import emoji
from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sql_tablet.mentors_dp import sql_command_random


async def start_command(message: types.Message) -> None:
    chat_id = message.chat.id
    await bot.send_message(message.chat.id, f"добро пожаловать {message.from_user.full_name}")
    await message.answer_sticker("CAACAgIAAxkBAAOVZIeqkNbQq5NRMhn8Qcf1qWdxgwgAAgQAAyAZghFiMCusGHQh0C8E")
    photo = open(r"/Users/klim/Desktop/Новая папка 2/images.jpeg", 'rb')
    await bot.send_photo(chat_id, photo=photo)


async def send_photo(message):
    chat_id = message.chat.id
    photo = open(r"/Users/klim/Desktop/Новая папка 2/chernyj-vlastelin_63116550_orig_.jpg", 'rb')
    await bot.send_photo(chat_id, photo=photo)


async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("ДАЛЕЕ", callback_data="next_button_1")
    markup.add(next_button)
    quiestion = "What year was Python introduced?"
    answers = [
        "1975-1977",
        "1980-1982",
        "1989-1991",
        "1967-1969",
        "1970-1973",
    ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Ты обязан это знать!",
        open_period=15,
        reply_markup=markup
    )


async def get_emoji(message: types.Message):
    emoji1 = ':face_savoring_food:'
    await bot.send_message(message.chat.id, emoji.emojize(emoji1))


async def get_random_mentor(message: types.Message) -> None:
    random_mentor = await sql_command_random()
    await message.answer(
                         f" name -> {random_mentor[1]} \n"
                         f"  age -> {random_mentor[2]} \n "
                         f" group -> {random_mentor[3]} \n "
                         f" direction ->  {random_mentor[4]}"
                                       )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(send_photo, commands=['mem'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(emoji, commands=['emoji'])
    dp.register_message_handler(get_random_mentor, commands=['get'])
