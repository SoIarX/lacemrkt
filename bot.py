from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
import keyboards as kb

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

print('bot started!')

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "🍇 Приветствую тебя в LASE MARKET!\n❔ Наши преимущества:\n🔥 Маленькие цены\n💨 Быстрое начисление голды\n👍 Начисление голды по айди(через сайт)\n👻 Удачных покупок:)!", reply_markup=kb.markup777)
    
@dp.message_handler(text='Купить Голду/Buy Gold 🌟')
async def process_buygold_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Выбери кол-во голды", reply_markup=kb.inline_kb1)
    
@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '100G • 69₽\n\nСпособы оплаты:\nQIWI/КАРТА: https://qiwi.com/n/FOLZ91 (rub) \n\nКАРТА/PAYEER/+: https://new.donatepay.ru/@1048895 (rub,dollar,uah)\n\nПосле оплаты отправляем скриншот оплаты + свой id в standoff 2 в бота (перейти в бота по кнопке ниже)', reply_markup=kb.urlkb)
    
@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '500G • 249₽\n\nСпособы оплаты:\nQIWI/КАРТА: https://qiwi.com/n/FOLZ91 (rub) \n\nКАРТА/PAYEER/+: https://new.donatepay.ru/@1048895 (rub,dollar,uah)\n\nПосле оплаты отправляем скриншот оплаты + свой id в standoff 2 в бота (перейти в бота по кнопке ниже', reply_markup=kb.urlkb)
    
@dp.callback_query_handler(lambda c: c.data == 'button3')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '1000G • 499₽\n\nСпособы оплаты:\nQIWI/КАРТА: https://qiwi.com/n/FOLZ91 (rub) \n\nКАРТА/PAYEER/+: https://new.donatepay.ru/@1048895 (rub,dollar,uah)\n\nПосле оплаты отправляем скриншот оплаты + свой id в standoff 2 в бота (перейти в бота по кнопке ниже', reply_markup=kb.urlkb)
    
@dp.callback_query_handler(lambda c: c.data == 'button4')
async def process_callback_button4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '3000G • 799₽\n\nСпособы оплаты:\nQIWI/КАРТА: https://qiwi.com/n/FOLZ91 (rub) \n\nКАРТА/PAYEER/+: https://new.donatepay.ru/@1048895 (rub,dollar,uah)\n\nПосле оплаты отправляем скриншот оплаты + свой id в standoff 2 в бота (перейти в бота по кнопке ниже', reply_markup=kb.urlkb)
    
@dp.callback_query_handler(lambda c: c.data == 'button5')
async def process_callback_button5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '5000G • 999₽\n\nСпособы оплаты:\nQIWI/КАРТА: https://qiwi.com/n/FOLZ91 (rub) \n\nКАРТА/PAYEER/+: https://new.donatepay.ru/@1048895 (rub,dollar,uah)\n\nПосле оплаты отправляем скриншот оплаты + свой id в standoff 2 в бота (перейти в бота по кнопке ниже', reply_markup=kb.urlkb)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)
    
if __name__ == '__main__':
    executor.start_polling(dp)