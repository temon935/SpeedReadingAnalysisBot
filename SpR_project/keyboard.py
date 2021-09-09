from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


# Кнопки и клавиатура главного меню
btnBookSlct = InlineKeyboardButton('Выбрать', callback_data='1')
btnAddBook = KeyboardButton('Добавить книгу', callback_data='2')

high_lvl_kb1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnBookSlct)
high_lvl_kb2 = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(btnAddBook)


