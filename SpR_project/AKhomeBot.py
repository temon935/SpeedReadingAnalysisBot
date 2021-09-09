import Brain
import config
import logging
import asyncio
import keyboard as kb
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as md
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


menu_list = []
# создаём форму и указываем поля
class Form(StatesGroup):
    title = State()
    img = State()
    num_of_pg = State()
    num_of_words = State()


# Начинаем наш диалог
@dp.message_handler(commands=['add'])
async def cmd_start(message: types.Message):
    await Form.title.set()
    await message.reply("Как называется книга")


# Добавляем возможность отмены, если пользователь передумал заполнять
@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('ОК')


# Сюда приходит ответ с названием книги
@dp.message_handler(state=Form.title)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['title'] = message.text

    await Form.next()
    await message.reply("Отправьте URL обложки книги")


# Принимаем обложку и узнаём кол-во страниц
@dp.message_handler(state=Form.img)
async def process_img(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['img'] = message.text

    await Form.next()
    await message.reply("Укажите количество страниц в книге?")


# Проверяем кол-во страниц
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.num_of_pg)
async def process_num_of_pg_invalid(message: types.Message):
    return await message.reply("Напиши кол-во страниц или напиши /cancel")


# Принимаем кол-во страниц и узнаём кол-во слов на странице
@dp.message_handler(lambda message: message.text.isdigit(), state=Form.num_of_pg)
async def process_num_of_pg(message: types.Message, state: FSMContext):
    await Form.next()
    await state.update_data(num_of_pg=int(message.text))
    await message.reply("Укажите количество слов на странице. Требуется 1 раз для 1-й книги.")


# Проверяем кол-во слов на странице
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.num_of_words)
async def process_num_of_words_invalid(message: types.Message):
    return await message.reply("Напиши кол-во слов или напиши /cancel")


# Принимаем слов на странице и выводим анкету
@dp.message_handler(lambda message: message.text.isdigit(), state=Form.num_of_words)
async def process_num_of_pg(message: types.Message, state: FSMContext):
    await state.update_data(num_of_words=int(message.text))
    async with state.proxy() as data:
        markup = types.ReplyKeyboardRemove()
        await bot.send_photo(message.chat.id, data['img'])
        await bot.send_message(
            message.chat.id,
            md.text(
                md.text(md.bold(data['title'])),
                # md.text('Обложка:', data['img']),
                md.text('Кол-во страниц:', data['num_of_pg']),
                md.text('Кол-во страниц:', data['num_of_words']),
                sep='\n',
            ),
            reply_markup=markup,
            parse_mode=ParseMode.MARKDOWN,
        )
        menu_list.append(data['title'])
        menu_list.append(data['img'])
        menu_list.append(data['num_of_pg'])
        menu_list.append(data['num_of_words'])
        await rec_data(menu_list)
        await state.finish()


async def rec_data(list_of_book_data):
    Brain.rec(list_of_book_data)


"""@dp.message_handler(commands=['menu'])
async def cmd_start(message: types.Message):
    for i in menu_list:
        await bot.send_photo(message.chat.id, i, reply_markup=kb.high_lvl_kb1)"""

# Сбор инфы о книге идет в лист. Требуется реализовать передачу данных на носитель, реализовать кнопки выбора




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
