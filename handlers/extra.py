from aiogram import types, Dispatcher
from config import bot


async def echo_text(message: types.Message) -> None:
    bad_words = ['дурак', 'html', 'js']
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            # await bot.delete_message(message.chat.id, message.message_id)
            await message.delete()
            await message.answer(
                f"Не матерись @{message.from_user.username}\n"
                f"сам ты {word}"
            )

            if message.text.startswith('.'):
                await bot.pin_chat_message(message.chat.id, message.message_id)


async def echo_message(msg: types.Message):
    if msg.text.isdigit():
         echo_text = int(msg.text) ** 2
    else:
         echo_text = msg.text
    await bot.send_message(msg.chat.id, echo_text)


async def echo_sticker(message: types. Message) -> None:
    await bot. send_sticker(message.chat.id, message.sticker.file_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_message, content_types=['text'])
    dp.register_message_handler(echo_sticker, content_types=['text'])