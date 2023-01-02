from aiogram import Router, F
from aiogram.filters import Command, Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from handlers.filters import ContainFilter, RegexFilter
from handlers.registration.filters import MinAgeFilter
from handlers.tools import REGISTRATION_DEFS, decline_age
from keyboards.registration import kb_init_profile, kb_genders
from states.registration import RegistrationStore

registration_router = Router()


@registration_router.message(Command('start'))
async def start(msg: Message, state: FSMContext):
    print("start stage")
    await msg.reply('Создайте анкету, чтобы продолжить!', reply_markup=kb_init_profile)
    await state.set_state(RegistrationStore.start)


@registration_router.message(Text('Сформировать анкету'), RegistrationStore.start)
async def accept_create(msg: Message, state: FSMContext):
    print("start create stage")
    await msg.reply('Как вас зовут?', reply_markup=kb_init_profile)
    await state.set_state(RegistrationStore.name)


@registration_router.message(~RegexFilter(REGISTRATION_DEFS['name_regex']), RegistrationStore.name)
async def incorrect_name(msg: Message, state: FSMContext):
    print("incorrect name")
    await msg.reply('Введите корректное имя.')


@registration_router.message(RegistrationStore.name)
async def name(msg: Message, state: FSMContext):
    print("name stage")
    await state.update_data(name=msg.text)
    await msg.reply('Какого вы пола?', reply_markup=kb_genders)
    await state.set_state(RegistrationStore.gender)


@registration_router.message(~ContainFilter(REGISTRATION_DEFS['genders'].values()), RegistrationStore.gender)
async def incorrect_gender(msg: Message):
    print("incorrect gender")
    await msg.reply('Выберите корректное значение пола.')


@registration_router.message(RegistrationStore.gender)
async def gender(msg: Message, state: FSMContext):
    print('gender stage')
    await state.update_data(gender=msg.text)
    await msg.reply('Сколько вам лет?')
    await state.set_state(RegistrationStore.age)


@registration_router.message(RegistrationStore.age, ~F.text.isdigit())
async def incorrect_age(msg: Message):
    print('incorrect age')
    await msg.reply('Введите корректное значение возраста.')


@registration_router.message(RegistrationStore.age, ~MinAgeFilter(REGISTRATION_DEFS['min_age']))
async def min_age(msg: Message):
    print('>14 age')
    await msg.reply(
        f'Наш проект недоступен лицам возрастом менее {decline_age(REGISTRATION_DEFS["min_age"])}. Введите допустимый '
        f'возраст.')


@registration_router.message(RegistrationStore.age)
async def age(msg: Message, state: FSMContext):
    await state.update_data(age=int(msg.text))
    print("age stage", await state.get_data())
    await state.set_state(RegistrationStore.city)
    await msg.reply('В каком городе вы находитесь?')


@registration_router.message(RegistrationStore.city)
async def city(msg: Message, state: FSMContext):
    print('city stage ')
    await state.update_data(city=msg.text)
    await msg.reply('Анкета успешно заполнена!')
    print(await state.get_data())