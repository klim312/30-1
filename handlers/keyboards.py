from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")
mem_button = KeyboardButton("/mem")
emoji_button = KeyboardButton("/emoji")
dice_button = KeyboardButton("/dice")
start_markup.add(
    start_button,
    quiz_button,
    mem_button,
    emoji_button,
    dice_button,
)