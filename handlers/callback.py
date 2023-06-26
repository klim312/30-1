from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("Далее", callback_data="next_button_2")
    markup.add(next_button)

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
        reply_markup=markup
    )


async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("Далее", callback_data="next_button_3")
    markup.add(next_button)

    quiestion = "what year was the internet invented"
    answers = [
        "1969",
        "1976",
        "1989",
        "1998",
        "1965",
        "1983",
   ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="грех не знать!",
        open_period=15,
        reply_markup=markup
    )


async def quiz_4(callback: types.CallbackQuery):
    await callback.message.answer("The End!")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
    dp.register_callback_query_handler(quiz_4, text="next_button_3")