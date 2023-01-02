from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton

btns_init_profile = [[KeyboardButton(text='Сформировать анкету')]]
kb_init_profile = ReplyKeyboardMarkup(keyboard=btns_init_profile, resize_keyboard=True, selective=True)


btns_genders = [[KeyboardButton(text='Женский'), KeyboardButton(text='Мужской')]]
kb_genders = ReplyKeyboardMarkup(keyboard=btns_genders, resize_keyboard=True, selective=True)
