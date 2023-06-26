from aiogram import types, Dispatcher
from config import bot


async def echo_text(message: types.Message) -> None:
    bad_words = ['дурак', 'html', 'js']
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            await message.delete()
            await message.answer(
                f"Не матерись @{message.from_user.username}\n"
                f"сам ты {word}"
            )

            if message.text.startswith('.'):
                await bot.pin_chat_message(message.chat.id, message.message_id)


async def echo(message: types.Message) -> None:
    if message.text.isdigit():
        n = int(message.text)**2
        await bot.send_message(message.chat.id, f"-->{n }")
    else:
        await bot.send_message(message.chat.id,f"[{message.text}]" )
# 🎲🎯🎰🎳🏀⚽️


async def echo_sticker(message: types. Message) -> None:
    await bot. send_sticker(message.chat.id, message.sticker.file_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo, content_types=['text'])
    dp.register_message_handler(echo_sticker, content_types=['text'])