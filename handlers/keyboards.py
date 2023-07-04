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
reg_button = KeyboardButton("/reg")

start_markup.add(
    start_button,
    quiz_button,
    mem_button,
    emoji_button,
    dice_button,
    reg_button,
)
cancel_button = KeyboardButton("отмена")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    cancel_button
)


submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("ДА"),
    KeyboardButton("СНОВА"),
    cancel_button
)
