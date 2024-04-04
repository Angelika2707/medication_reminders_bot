from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.keyboard import select_language, select_time_zone_ru, select_time_zone_en
from app.states import RegistrationUser
from aiogram.fsm.context import FSMContext
from app.database.requests import insert_user, check_registered_user, insert_new_settings

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    await state.set_state(RegistrationUser.language)
    await message.answer(
        "Привет, я бот! Помогаю отслеживать пить таблетки каждый день\n\nВыберете язык, чтобы я мог рассказать больше",
        reply_markup=select_language)


@router.message(Command("help"))
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


@router.message(RegistrationUser.time_zone, F.text.in_({"Мск", "Мск+1", "Мск-1", "Msc", "Msc+1", "Msc-1"}))
async def time_zone_markup(message: Message, state: FSMContext) -> None:
    await state.update_data(time_zone=message.text)
    user_language = await state.get_data()

    if await check_registered_user(str(message.from_user.id)):
        await insert_new_settings(str(message.from_user.id), user_language["language"], user_language["time_zone"])
        print("Обновлены данные пользователя:", message.from_user.id)
    else:
        print("добавден новый пользователь:", message.from_user.id)
        await insert_user(str(message.from_user.id), user_language["language"], user_language["time_zone"])

    if user_language["language"] == "RU":
        await message.answer(
            "Настройка бота завершена!\nЕсли захотите изменить их, воспользуйтесь командой /start",
            reply_markup=select_time_zone_ru)
    else:
        await message.answer(
            "The bot configuration is complete!\nIf you want to change them, use the command /start",
            reply_markup=select_time_zone_en)
    await state.clear()


@router.message(RegistrationUser.time_zone, ~F.text.in_({"Мск", "Мск+1", "Мск-1", "Msc", "Msc+1", "Msc-1"}))
async def time_zone_markup(message: Message, state: FSMContext) -> None:
    user_language = await state.get_data()
    if user_language["language"] == "RU":
        await message.answer(
            "Выберете часовой пояс на клавиатуре",
            reply_markup=select_time_zone_ru)
    else:
        await message.answer(
            "Select the time zone on your keyboard",
            reply_markup=select_time_zone_en)


@router.message(RegistrationUser.language, F.text.in_({"RU", "EN"}))
async def time_zone_markup(message: Message, state: FSMContext) -> None:
    await state.set_state(RegistrationUser.time_zone)

    await state.update_data(language=message.text)
    if message.text == "RU":
        await message.answer(
            "Выберете часовой пояс в котором ты чаще всего находишься",
            reply_markup=select_time_zone_ru)
    else:
        await message.answer(
            "Choose the time zone you are most often in",
            reply_markup=select_time_zone_en)


@router.message(RegistrationUser.language, ~F.text.in_({"RU", "EN"}))
async def time_zone_markup(message: Message) -> None:
    await message.answer(
        "Выберете язык на клавиатуре",
        reply_markup=select_language)
