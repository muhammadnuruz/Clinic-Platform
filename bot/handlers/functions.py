import json
import os
from urllib.parse import quote

import aiohttp
import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from bot.buttons.reply_buttons import back_main_menu_button, main_menu_buttons
from bot.buttons.text import contact, contact_ru, social_networks, social_networks_ru, location, location_ru, \
    ask_question_ru, ask_question, search_analyses, search_analyses_ru, get_analyses_result, get_analyses_result_ru
from bot.dispatcher import dp, bot
from main import admins


@dp.message_handler(Text(equals=[contact, contact_ru]))
async def contact_function(msg: types.Message):
    if msg.text == contact:
        await msg.answer(text='Yagona telefon raqami: +998912787878')
    else:
        await msg.answer(text='Единственный номер телефона: +998912787878')


@dp.message_handler(Text(equals=[social_networks, social_networks_ru]))
async def sociable_networks_function(msg: types.Message):
    if msg.text == social_networks:
        await msg.answer(text="""
Bizning ijtimoiy tarmoqlarga obuna bo'ling 👇:

Instagram: https://www.instagram.com/arzon.lab/
YouTube: https://youtube.com/@arzonlab
Facebook: https://www.facebook.com/profile.php?id=61558339262051
Telegram: https://t.me/arzonlab""")
    else:
        await msg.answer(text="""
Подписывайтесь на наши социальные сети 👇:

Instagram: https://www.instagram.com/arzon.lab/
YouTube: https://youtube.com/@arzonlab
Facebook: https://www.facebook.com/profile.php?id=61558339262051
Telegram: https://t.me/arzonlab""")


@dp.message_handler(Text(equals=[location, location_ru]))
async def contact_function(msg: types.Message):
    await msg.answer(text=msg.text)
    await msg.answer_location(latitude=41.365333, longitude=69.293618)


@dp.message_handler(Text(equals=[ask_question, ask_question_ru]))
async def ask_question_function(msg: types.Message, state: FSMContext):
    await state.set_state('ask_question')
    if msg.text == ask_question:
        await msg.answer(
            text="Talab va istaklaringizni yozib qoldiring va biz albatta ko'rib chiqib yechim topishga harakat qilamiz:",
            reply_markup=await back_main_menu_button(msg.from_user.id))
    else:
        await msg.answer(text="Запишите ваши требования и пожелания и мы обязательно постараемся найти решение:",
                         reply_markup=await back_main_menu_button(msg.from_user.id))


@dp.message_handler(state='ask_question')
async def receive_question_and_notify_admins(msg: types.Message, state: FSMContext):
    user_info = f"User ID: <a href='tg://user?id={msg.from_user.id}'>{msg.from_user.id}</a>\n" \
                f"Username: @{msg.from_user.username}\n" \
                f"Ism-Familiya: {msg.from_user.full_name}\n" \
                f"Xabar: {msg.text}"
    for admin in admins:
        await bot.send_message(chat_id=admin, text=user_info, parse_mode='HTML')
    tg_user = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{msg.from_user.id}/").content)
    if tg_user['language'] == 'uz':
        await msg.answer(text="Xabaringiz adminlarga jo'natildi!",
                         reply_markup=await main_menu_buttons(msg.from_user.id))
    else:
        await msg.answer(text="Ваше сообщение отправлено администраторам!",
                         reply_markup=await main_menu_buttons(msg.from_user.id))
    await state.finish()


@dp.message_handler(Text(equals=[search_analyses, search_analyses_ru]))
async def start_analysis_search(msg: types.Message, state: FSMContext):
    await state.set_state('search_type')
    if msg.text == search_analyses:
        await msg.answer(text="Iltimos, analiz nomini kiriting:",
                         reply_markup=await back_main_menu_button(msg.from_user.id))
    else:
        await msg.answer(text="Пожалуйста, введите название анализа:",
                         reply_markup=await back_main_menu_button(msg.from_user.id))


@dp.message_handler(state='search_type')
async def process_analysis_name(msg: types.Message, state: FSMContext):
    tg_user = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{msg.from_user.id}/").content)
    response = requests.get(f"http://127.0.0.1:8000/api/types/search/{msg.text}/")
    if response.status_code == 200:
        analysis_data = response.json()
        if analysis_data:
            if tg_user['language'] == 'uz':
                result = (
                    f"🔎 Natija:\n\n"
                    f"📝 Nomi: {analysis_data.get('name', 'Nomalum')}\n"
                    f"💵 Narxi: {analysis_data.get('price', 'Nomalum')} so'm\n"
                    f"ℹ️ Ma'lumot: {analysis_data.get('info', 'Malumot mavjud emas')}\n"
                    f"🕒 Tayyor bo'lish vaqti: {analysis_data.get('to_be_ready', 'Nomalum')} kun"
                )
            else:
                result = (
                    f"🔎 Результат:\n\n"
                    f"📝 Название: {analysis_data.get('ru_name', 'Неизвестно')}\n"
                    f"💵 Цена: {analysis_data.get('price', 'Неизвестно')} сум\n"
                    f"ℹ️ Информация: {analysis_data.get('ru_info', 'Информация отсутствует')}\n"
                    f"🕒 Время готовности: {analysis_data.get('to_be_ready', 'Неизвестно')} день"
                )

            await msg.answer(result, reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer(
                "❌ Bu nomga mos analiz topilmadi." if tg_user[
                                                          'language'] == 'uz' else "❌ Анализ с таким названием не найден.",
                reply_markup=await main_menu_buttons(msg.from_user.id))
    else:
        await msg.answer(
            "❌ Bu nomga mos analiz topilmadi." if tg_user[
                                                      'language'] == 'uz' else "❌ Анализ с таким названием не найден.",
            reply_markup=await main_menu_buttons(msg.from_user.id))

    await state.finish()


@dp.message_handler(Text(equals=[get_analyses_result, get_analyses_result_ru]))
async def search_analysis_handler(msg: types.Message, state: FSMContext):
    if msg.text == get_analyses_result:
        await msg.answer("Iltimos, analizning ID raqamini kiriting:",
                         reply_markup=await back_main_menu_button(msg.from_user.id))
    else:
        await msg.answer("Пожалуйста, введите идентификационный номер анализа:",
                         reply_markup=await back_main_menu_button(msg.from_user.id))
    await state.set_state('waiting_for_analysis_id')


@dp.message_handler(state='waiting_for_analysis_id')
async def process_analysis_id(msg: types.Message, state: FSMContext):
    analysis_id = msg.text
    tg_user = json.loads(
        requests.get(url=f"http://127.0.0.1:8000/api/telegram-users/chat_id/{msg.from_user.id}/").content)

    if not analysis_id.isdigit():
        if tg_user['language'] == 'uz':
            await msg.answer("❌ Iltimos, to'g'ri ID kiriting.")
        else:
            await msg.answer("❌ Пожалуйста, введите действительный идентификатор.")
        return

    response = requests.get(f"http://127.0.0.1:8000/api/analyses/{analysis_id}/")

    if response.status_code == 200:
        analysis_data = response.json()

        temp_file_path = f"/tmp/{os.path.basename(analysis_data.get('file'))}"

        async with aiohttp.ClientSession() as session:
            async with session.get(analysis_data.get('file')) as resp:
                if resp.status == 200:
                    with open(temp_file_path, 'wb') as f:
                        f.write(await resp.read())

        await msg.answer_document(document=types.InputFile(temp_file_path),
                                  reply_markup=await main_menu_buttons(msg.from_user.id))

        os.remove(temp_file_path)

    else:
        if tg_user['language'] == 'uz':
            await msg.answer("❌ Bu ID ga mos analiz topilmadi.", reply_markup=await main_menu_buttons(msg.from_user.id))
        else:
            await msg.answer("❌ Анализ по этому идентификатору не найден.",
                             reply_markup=await main_menu_buttons(msg.from_user.id))

    await state.finish()
