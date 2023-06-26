from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from . import keyboards
from config import master_admin, tutor_admin


class UserState(StatesGroup):
    name = State()
    age = State()
    group = State()
    direction = State()
    submit = State()


async def mentor_register(message: types.Message):
    if message.from_user.id not in master_admin and tutor_admin:
        await message.answer("Вы не обладаете правами Администратора!")
    else:
        await message.answer(f"Добро пожаловать! {message.from_user.full_name}")
        if message.chat.type == 'private':
            await UserState.name.set()
            await message.answer("Имя ментора? ", reply_markup=keyboards.cancel_markup)
        else:
            await message.reply("Пиши в личке!")


async def get_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await message.answer("Возраст ментора? .", reply_markup=keyboards.cancel_markup)
        await UserState.next()


async def get_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await message.answer("Введите группу ментора .", reply_markup=keyboards.cancel_markup)
        await UserState.next()


async def get_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await message.answer("Направление ментора? .", reply_markup=keyboards.cancel_markup)
    await UserState.next()


async def get_dion(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['напрвление'] = message.text
    await message.answer(f"Имя: {data['name']}\n"
                         f"Возраст: {data['age']}\n"
                         f"Группа: {data['group']}\n"
                         f"Напрвление: {data['direction']}\n")
    await UserState.next()
    await message.answer("Все верно?", reply_markup=keyboards.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'Да':
        # TODO: Запись в БД
        await state.finish()
        await message.answer("Отлично!записал в БД!")
    elif message.text.lower() == 'Снова':
        await message.answer("Пиши команду -> /reg")
        await state.finish()
    else:
        await message.answer("Воспользуйся кнопками!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
    else:
        await message.answer("Не отменяй!""/start!")


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(mentor_register, commands=['reg'])
    dp.register_message_handler(get_name, state=UserState.name)
    dp.register_message_handler(get_age, state=UserState.age)
    dp.register_message_handler(get_group, state=UserState.group)
    dp.register_message_handler(get_dion, state=UserState.direction)
    dp.register_message_handler(submit, state=UserState.submit)
