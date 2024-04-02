from aiogram.fsm.state import StatesGroup, State


class RegistrationUser(StatesGroup):
    language = State()
    time_zone = State()
