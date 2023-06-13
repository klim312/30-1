from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    chat_id = message.chat.id
    await bot.send_message(message.chat.id, f"добро пожаловать {message.from_user.full_name}")
    await message.answer_sticker("CAACAgIAAxkBAAOVZIeqkNbQq5NRMhn8Qcf1qWdxgwgAAgQAAyAZghFiMCusGHQh0C8E")
    photo = open(r"/Users/klim/Desktop/Новая папка 2/images.jpeg", 'rb')
    await bot.send_photo(chat_id, photo=photo)


@dp.message_handler(commands=['mem'])
async def send_photo(message):
    chat_id = message.chat.id
    photo = open(r"/Users/klim/Desktop/Новая папка 2/chernyj-vlastelin_63116550_orig_.jpg", 'rb')
    await bot.send_photo(chat_id, photo=photo)


@dp.message_handler(commands=['quiz'])
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

    # await bot.send_poll()
    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Ты обязан это знать!",
        open_period=10,
        reply_markup=markup
    )



@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text.isdigit():
        echo_text = int(msg.text) ** 2
    else:
        echo_text = msg.text
    await bot.send_message(msg.chat.id, echo_text)
@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "Who it Johnny Sins?"
    answers = [
        "Doctor",
        "Actor",
        "Neighbour",
        "Security guard",
        "Legend",
        "Vet",
    ]

    # await bot.send_poll()
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=4,
        explanation="Легенда!",
        open_period=15,
    )


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)


@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types. Message):
    await message.answer(message.sticker .file_id)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)