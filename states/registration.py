from aiogram.fsm.state import State, StatesGroup


class RegistrationStore(StatesGroup):
    start = State()
    name = State()
    gender = State()
    age = State()
    city = State()
