from aiogram import Router
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.accept_kb import accept_keyboard
from states.registration import RegistrationStore, ByeStore

router = Router()


@router.message(Command('start'), StateFilter(None))
async def cmd_start(msg: Message, state: FSMContext):
    await msg.reply("Привет, продолжим?", reply_markup=accept_keyboard)
    await state.set_state(RegistrationStore.started)


@router.message(ByeStore.bye)
async def bye(msg: Message, state: FSMContext):
    await msg.reply("бай-бай", reply_markup=ReplyKeyboardRemove())
    await state.set_state(None)


@router.message(RegistrationStore.started)
async def start_accept(msg: Message, state: FSMContext):
    await yes_or_no(msg, state, RegistrationStore.wait_name, ByeStore.bye, RegistrationStore.started)


@router.message(RegistrationStore.wait_name)
async def step_name(msg: Message, state: FSMContext):
    await msg.reply('Введите имя')
    await state.update_data(name=msg.text)
    await state.set_state(RegistrationStore.wait_age)


@router.message(RegistrationStore.wait_age)
async def step_age(msg: Message, state: FSMContext):
    await msg.reply('Введите возраст')
    await state.update_data(age=msg.text)
    await state.set_state(RegistrationStore.answer)


@router.message(RegistrationStore.answer)
async def step_answer(msg: Message, state: FSMContext):
    curr_state = await state.get_data()
    print(curr_state)
