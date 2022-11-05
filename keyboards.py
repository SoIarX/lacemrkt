from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

button1 = KeyboardButton('Купить Голду/Buy Gold 🌟')

markup777 = ReplyKeyboardMarkup(resize_keyboard=True).add(button1)





inline_btn_1 = InlineKeyboardButton('100G • 69₽', callback_data='button1')

inline_btn_2 = InlineKeyboardButton('500G • 249₽', callback_data='button2')

inline_btn_3 = InlineKeyboardButton('1000G • 499₽', callback_data='button3')

inline_btn_4 = InlineKeyboardButton('3000G • 799₽', callback_data='button4')

inline_btn_5 = InlineKeyboardButton('5000G • 999₽', callback_data='button5')

inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2).add(inline_btn_3).add(inline_btn_4).add(inline_btn_5)

urlkb = InlineKeyboardMarkup(row_width=1)
urlButton = InlineKeyboardButton(text='бот', url  = 'https://t.me/ProemgoldIubot')
urlkb.add(urlButton)