import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# ===== ТВОИ ДАННЫЕ =====
BOT_TOKEN = "8334628767:AAHeA3jjS95naU_CVZ0T_51GkOzHwgfZUX8"
CHANNEL_ID = -1003611050389

# ССЫЛКИ
TG_CHANNEL = "https://t.me/tairo_o"
TG_READY_WORKS = "https://t.me/tairo_o"
INSTAGRAM = "скоро будет"
REVIEWS_CHANNEL = "https://t.me/tairo_otzivi"
MANAGER_CONTACT = "https://t.me/tairo_manager"

# ФОТО ПРИМЕРОВ
PHOTO_KEY_EXAMPLE = "AgACAgIAAxkBAAMeae07hyGSB4324fMWh2PeZcq1QVgAAmYUaxvhqmhLZY21OokVpbIBAAMCAAN5AAM7BA"
PHOTO_MODEL_EXAMPLE = "AgACAgIAAxkBAAMgae07kB9viiyM9PNIqeZ_DwmrGGcAAm4VaxsVSmlLo8bb6Sy2YdIBAAMCAAN5AAM7BA"
PHOTO_7PHOTO_EXAMPLE = "AgACAgIAAxkBAAMiae07lhqBN3Qis2SRDppFgnxLrswAAnAVaxsVSmlLOzS1lngyfL0BAAMCAAN5AAM7BA"
# =======================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# ========== ГЛАВНОЕ МЕНЮ ==========
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🖼️ Наши готовые картины")],
        [KeyboardButton(text="🎨 Создать картину")],
        [KeyboardButton(text="📱 Наши соц. сети")],
        [KeyboardButton(text="👨‍💼 Менеджер")],
        [KeyboardButton(text="📝 Отзывы")]
    ],
    resize_keyboard=True
)

back_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="🔙 Назад / В начало")]],
    resize_keyboard=True
)

# ========== КЛАВИАТУРЫ ДЛЯ НАСТРОЕК ==========
size_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="20x30"), KeyboardButton(text="30x40")],
        [KeyboardButton(text="50x40"), KeyboardButton(text="50x70")],
        [KeyboardButton(text="70x90"), KeyboardButton(text="100x120")],
        [KeyboardButton(text="🔙 Назад / В начало")]
    ],
    resize_keyboard=True
)

orientation_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📐 Горизонтальная"), KeyboardButton(text="📏 Вертикальная")],
        [KeyboardButton(text="🔙 Назад / В начало")]
    ],
    resize_keyboard=True
)

light_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💡 Теплый белый"), KeyboardButton(text="❄️ Холодный белый")],
        [KeyboardButton(text="🌈 RGB"), KeyboardButton(text="🚫 Без подсветки")],
        [KeyboardButton(text="🔙 Назад / В начало")]
    ],
    resize_keyboard=True
)

background_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⚫ Черный"), KeyboardButton(text="⚪ Белый")],
        [KeyboardButton(text="🪵 Карбон"), KeyboardButton(text="✏️ Свой цвет")],
        [KeyboardButton(text="🔙 Назад / В начало")]
    ],
    resize_keyboard=True
)

# ========== СОСТОЯНИЯ ==========
class OrderKey(StatesGroup):
    waiting_for_size = State()
    waiting_for_orientation = State()
    waiting_for_light = State()
    waiting_for_background = State()
    waiting_for_key = State()
    waiting_for_phrase = State()
    waiting_for_badge = State()
    waiting_for_currency = State()
    waiting_for_confirm = State()

class OrderModelSpecs(StatesGroup):
    waiting_for_light = State()
    waiting_for_ref_photos = State()
    waiting_for_specs = State()
    waiting_for_confirm = State()

class OrderModel7Photo(StatesGroup):
    waiting_for_light = State()
    waiting_for_ref_photos = State()
    waiting_for_final_photos = State()
    waiting_for_confirm = State()

# Хранилище
user_data_store = {}
temp_albums = {}  # Для временного хранения альбомов

# ========== КОМАНДА /start ==========
@dp.message(Command("start"))
async def start_cmd(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        "🎨 Добро пожаловать в TAIRO!\n\nМы создаём мотивационные картины с твоим авто, ключом и стилем.\n\nВыбери действие:",
        reply_markup=main_menu
    )

@dp.message(lambda msg: msg.text == "🔙 Назад / В начало")
async def back_to_main(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("🏠 Главное меню", reply_markup=main_menu)

@dp.message(lambda msg: msg.text == "🖼️ Наши готовые картины")
async def ready_works(message: types.Message):
    await message.answer(
        f"🖼️ Наши готовые картины:\n\nhttps://t.me/tairo_o\n\nСмотри выбирай из готовых вариантов!",
        reply_markup=main_menu
    )

@dp.message(lambda msg: msg.text == "📱 Наши соц. сети")
async def social_networks(message: types.Message):
    await message.answer(
        f" *Наши соц. сети:*\n\n"
        f" [Тг канал](https://t.me/tairo_o)\n"
        
        f" [Тг бот](https://t.me/tairo_o_bot)\n"
        
        f" [Прайс лист](https://t.me/tairo_o/16)\n"
        
        f" [Тг менеджер](https://t.me/tairo_manager)\n"
        
        f" [Тг канал с отзывами](https://t.me/tairo_otzivi)\n"
        
        f" [Instagram](https://instagram.com/tairocustoms)\n"
        
        f" [Tiktok](https://tiktok.com/@tairocustoms)\n"
        
        f" [Vk паблик](https://vk.com/tairocustoms)\n"
        
        f" [Avito](https://www.avito.ru/user/2b07c3220477f96997e1d5148950ad25/profile?src=sharing)\n\n"
        
        f"TAIRO | Картины твоей мотивации",
        parse_mode="Markdown",
        reply_markup=main_menu
    )
@dp.message(lambda msg: msg.text == "👨‍💼 Менеджер")
async def manager_contact(message: types.Message):
    await message.answer(
        f"👨‍💼 Написать нашему менеджеру:\n\n{MANAGER_CONTACT}\n\nОн ответит на все вопросы и поможет с заказом.",
        reply_markup=main_menu
    )

@dp.message(lambda msg: msg.text == "📝 Отзывы")
async def reviews(message: types.Message):
    await message.answer(
        f"⭐ Наши отзывы:\n\n{REVIEWS_CHANNEL}\n\nСпасибо, что выбираете TAIRO!",
        reply_markup=main_menu
    )

# ========== СОЗДАТЬ КАРТИНУ ==========
@dp.message(lambda msg: msg.text == "🎨 Создать картину")
async def create_painting(message: types.Message, state: FSMContext):
    await state.clear()
    
    result = await message.answer_media_group(
        media=[
            types.InputMediaPhoto(media=PHOTO_KEY_EXAMPLE, caption="🔑 Ключ + купюры"),
            types.InputMediaPhoto(media=PHOTO_MODEL_EXAMPLE, caption="📊 Модель с характеристиками"),
            types.InputMediaPhoto(media=PHOTO_7PHOTO_EXAMPLE, caption="🖼️ Модель с лого и 7 фото")
        ]
    )
    
    if result:
        user_data_store[message.from_user.id] = {
            "example_message_ids": [msg.message_id for msg in result]
        }
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔑 Ключ + купюры", callback_data="choose_key")],
        [InlineKeyboardButton(text="📊 Модель с характеристиками", callback_data="choose_model_specs")],
        [InlineKeyboardButton(text="🖼️ Модель с лого и 7 фото", callback_data="choose_model_7photo")],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")]
    ])
    
    await message.answer("👇 Выбери тип картины:", reply_markup=keyboard)

async def delete_unwanted_photos(user_id, keep_index):
    if user_id not in user_data_store:
        return
    example_ids = user_data_store[user_id].get("example_message_ids", [])
    for i, msg_id in enumerate(example_ids):
        if i != keep_index:
            try:
                await bot.delete_message(user_id, msg_id)
            except:
                pass

# ========== КЛЮЧ + КУПЮРЫ ==========
@dp.callback_query(lambda c: c.data == "choose_key")
async def choose_key(callback: types.CallbackQuery, state: FSMContext):
    await delete_unwanted_photos(callback.from_user.id, keep_index=0)
    await callback.message.delete()
    await state.set_state(OrderKey.waiting_for_size)
    await callback.message.answer(
        "📏 Шаг 1 из 8: Размер рамки\n\nВыбери размер картины:",
        reply_markup=size_kb
    )
    await callback.answer()

@dp.message(OrderKey.waiting_for_size)
async def get_size(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if message.text not in ["20x30", "30x40", "50x40", "50x70", "70x90", "100x120"]:
        await message.answer("Пожалуйста, выбери размер из кнопок")
        return
    await state.update_data(size=message.text)
    await state.set_state(OrderKey.waiting_for_orientation)
    await message.answer(
        "🖼️ Шаг 2 из 8: Ориентация картины\n\nВыбери ориентацию:",
        reply_markup=orientation_kb
    )

@dp.message(OrderKey.waiting_for_orientation)
async def get_orientation(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if message.text not in ["📐 Горизонтальная", "📏 Вертикальная"]:
        await message.answer("Пожалуйста, выбери ориентацию из кнопок")
        return
    await state.update_data(orientation=message.text)
    await state.set_state(OrderKey.waiting_for_light)
    await message.answer(
        "💡 Шаг 3 из 8: Цвет подсветки\n\nВыбери подсветку для картины:",
        reply_markup=light_kb
    )

@dp.message(OrderKey.waiting_for_light)
async def get_light(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if message.text not in ["💡 Теплый белый", "❄️ Холодный белый", "🌈 RGB", "🚫 Без подсветки"]:
        await message.answer("Пожалуйста, выбери подсветку из кнопок")
        return
    await state.update_data(light=message.text)
    await state.set_state(OrderKey.waiting_for_background)
    await message.answer(
        "🎨 Шаг 4 из 8: Цвет фона\n\nВыбери цвет фона или напиши свой:",
        reply_markup=background_kb
    )

@dp.message(OrderKey.waiting_for_background)
async def get_background(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    background = message.text
    await state.update_data(background=background)
    await state.set_state(OrderKey.waiting_for_key)
    await message.answer(
        "🔑 Шаг 5 из 8: Ключ\n\nПришли фото ключа или напиши текстом",
        reply_markup=back_button
    )

@dp.message(OrderKey.waiting_for_key)
async def get_key(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if message.photo:
        await state.update_data(key_photo=message.photo[-1].file_id, key_text=None)
    else:
        await state.update_data(key_text=message.text, key_photo=None)
    await state.set_state(OrderKey.waiting_for_phrase)
    await message.answer("📝 Шаг 6 из 8: Фраза\n\nНапиши мотивационную фразу", reply_markup=back_button)

@dp.message(OrderKey.waiting_for_phrase)
async def get_phrase(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    await state.update_data(phrase=message.text)
    await state.set_state(OrderKey.waiting_for_badge)
    await message.answer("🏷️ Шаг 7 из 8: Шильдик\n\nПришли фото шильдика или напиши текст", reply_markup=back_button)

@dp.message(OrderKey.waiting_for_badge)
async def get_badge(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if message.photo:
        await state.update_data(badge_photo=message.photo[-1].file_id, badge_text=None)
    else:
        await state.update_data(badge_text=message.text, badge_photo=None)
    await state.set_state(OrderKey.waiting_for_currency)
    currency_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="$"), KeyboardButton(text="€")],
            [KeyboardButton(text="₽"), KeyboardButton(text="£")],
            [KeyboardButton(text="✏️ Своя валюта")],
            [KeyboardButton(text="🔙 Назад / В начало")]
        ],
        resize_keyboard=True
    )
    await message.answer("💰 Шаг 8 из 8: Валюта\n\nВыбери валюту:", reply_markup=currency_kb)

@dp.message(OrderKey.waiting_for_currency)
async def get_currency(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    await state.update_data(currency=message.text)
    await state.set_state(OrderKey.waiting_for_confirm)
    data = await state.get_data()
    
    confirm_text = f"📋 ПРОВЕРЬ ЗАКАЗ (Ключ + купюры)\n\n📏 Размер: {data.get('size', '—')}\n🖼️ Ориентация: {data.get('orientation', '—')}\n💡 Подсветка: {data.get('light', '—')}\n🎨 Цвет фона: {data.get('background', '—')}\n\n📝 Фраза: {data.get('phrase', '—')}\n💰 Валюта: {message.text}\n🔑 Ключ: {data.get('key_text', 'фото')}\n🏷️ Шильдик: {data.get('badge_text', 'фото')}\n\n✅ Всё верно?\n❌ Или начать сначала?"
    
    confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Да, отправить заказ", callback_data="confirm_key_send")],
        [InlineKeyboardButton(text="🔄 Переделать сначала", callback_data="confirm_cancel")]
    ])
    
    media_group = []
    if data.get('key_photo'):
        media_group.append(types.InputMediaPhoto(media=data['key_photo'], caption="🔑 Ключ"))
    if data.get('badge_photo'):
        media_group.append(types.InputMediaPhoto(media=data['badge_photo'], caption="🏷️ Шильдик"))
    
    if media_group:
        await message.answer_media_group(media_group)
    await message.answer(confirm_text, reply_markup=confirm_kb)

@dp.callback_query(lambda c: c.data == "confirm_key_send")
async def confirm_key_send(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    username = callback.from_user.username or callback.from_user.first_name
    
    order_text = f"🔥 НОВЫЙ ЗАКАЗ (Ключ + купюры)\n\n👤 Клиент: @{username}\n\n📏 Размер: {data.get('size', '—')}\n🖼️ Ориентация: {data.get('orientation', '—')}\n💡 Подсветка: {data.get('light', '—')}\n🎨 Цвет фона: {data.get('background', '—')}\n\n📝 Фраза: {data.get('phrase', '—')}\n💰 Валюта: {data.get('currency', '—')}\n🔑 Ключ: {data.get('key_text', 'фото')}\n🏷️ Шильдик: {data.get('badge_text', 'фото')}"
    
    await bot.send_message(CHANNEL_ID, order_text)
    
    if data.get('key_photo'):
        await bot.send_photo(CHANNEL_ID, data['key_photo'], caption="🔑 Ключ")
    if data.get('badge_photo'):
        await bot.send_photo(CHANNEL_ID, data['badge_photo'], caption="🏷️ Шильдик")
    
    await callback.message.delete()
    await callback.message.answer("✅ Заказ отправлен мастеру! Мастер свяжется с тобой.", reply_markup=main_menu)
    await state.clear()
    await callback.answer()

@dp.callback_query(lambda c: c.data == "confirm_cancel")
async def confirm_cancel(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.delete()
    await callback.message.answer("🔄 Заказ отменён. Начнём сначала!\n\nНапиши /start", reply_markup=main_menu)
    await state.clear()
    await callback.answer()

# ========== МОДЕЛЬ С ХАРАКТЕРИСТИКАМИ (с поддержкой альбомов) ==========
@dp.callback_query(lambda c: c.data == "choose_model_specs")
async def choose_model_specs(callback: types.CallbackQuery, state: FSMContext):
    await delete_unwanted_photos(callback.from_user.id, keep_index=1)
    await callback.message.delete()
    await state.set_state(OrderModelSpecs.waiting_for_light)
    await state.update_data(ref_photos=[])
    await callback.message.answer(
        "💡 Выбери подсветку для картины:",
        reply_markup=light_kb
    )
    await callback.answer()

@dp.message(OrderModelSpecs.waiting_for_light)
async def get_light_specs(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if message.text not in ["💡 Теплый белый", "❄️ Холодный белый", "🌈 RGB", "🚫 Без подсветки"]:
        await message.answer("Пожалуйста, выбери подсветку из кнопок")
        return
    await state.update_data(light=message.text)
    await state.set_state(OrderModelSpecs.waiting_for_ref_photos)
    await message.answer(
        "📸 Пришли 4 фото авто с разных ракурсов\n\nЭто нужно чтобы мы могли максимально точно сделать модельку твоего авто",
        reply_markup=back_button
    )

@dp.message(OrderModelSpecs.waiting_for_ref_photos)
async def get_ref_photos_specs(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if not message.photo:
        await message.answer("Пожалуйста, пришли фото авто")
        return
    
    data = await state.get_data()
    existing_photos = data.get('ref_photos', []).copy()
    target = 4
    
    # Проверяем, является ли сообщение частью альбома
    if message.media_group_id:
        # Обрабатываем альбом
        media_group_id = message.media_group_id
        
        if media_group_id not in temp_albums:
            temp_albums[media_group_id] = {
                "photos": [],
                "user_id": message.from_user.id,
                "target": target
            }
        
        temp_albums[media_group_id]["photos"].append(message.photo[-1].file_id)
        await asyncio.sleep(1.5)
        
        if media_group_id in temp_albums:
            album_data = temp_albums.pop(media_group_id)
            new_photos = list(dict.fromkeys(album_data["photos"]))
        else:
            return
    else:
        # Обычное фото
        new_photos = [message.photo[-1].file_id]
    
    all_photos = existing_photos + new_photos
    all_photos = list(dict.fromkeys(all_photos))
    
    await state.update_data(ref_photos=all_photos)
    current = len(all_photos)
    
    if current >= target:
        all_photos = all_photos[:target]
        await state.update_data(ref_photos=all_photos)
        await state.set_state(OrderModelSpecs.waiting_for_specs)
        await message.answer(f"✅ Получено {target} фото!\n\n⚙️ Теперь пришли характеристики авто:\n\n• Марка + модель\n• Объем двигателя\n• Год\n• Мощность (л.с.)\n• Разгон 0-100\n• Свое(по желанию)", reply_markup=back_button)
    else:
        await message.answer(f"✅ Получено {current}/{target} фото. Пришли ещё {target - current}.")

@dp.message(OrderModelSpecs.waiting_for_specs)
async def get_specs(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    await state.update_data(specs=message.text)
    await state.set_state(OrderModelSpecs.waiting_for_confirm)
    data = await state.get_data()
    
    confirm_text = f"📋 ПРОВЕРЬ ЗАКАЗ (Модель с характеристиками)\n\n💡 Подсветка: {data.get('light', '—')}\n\n📊 Характеристики:\n{message.text}\n\n📸 Фото авто: {len(data.get('ref_photos', []))} шт.\n\n✅ Всё верно?\n❌ Или начать сначала?"
    
    confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Да, отправить заказ", callback_data="confirm_specs_send")],
        [InlineKeyboardButton(text="🔄 Переделать сначала", callback_data="confirm_cancel")]
    ])
    
    ref_photos = data.get('ref_photos', [])
    if ref_photos:
        media_group = [types.InputMediaPhoto(media=pid, caption=f"📸 Фото {i+1}") for i, pid in enumerate(ref_photos)]
        await message.answer_media_group(media_group)
    
    await message.answer(confirm_text, reply_markup=confirm_kb)

@dp.callback_query(lambda c: c.data == "confirm_specs_send")
async def confirm_specs_send(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    username = callback.from_user.username or callback.from_user.first_name
    
    order_text = f"🔥 НОВЫЙ ЗАКАЗ (Модель с характеристиками)\n\n👤 Клиент: @{username}\n\n💡 Подсветка: {data.get('light', '—')}\n\n📊 Характеристики:\n{data.get('specs', '—')}\n\n📸 Фото авто: {len(data.get('ref_photos', []))} шт."
    
    await bot.send_message(CHANNEL_ID, order_text)
    
    for pid in data.get('ref_photos', []):
        await bot.send_photo(CHANNEL_ID, pid)
    
    await callback.message.delete()
    await callback.message.answer("✅ Заказ отправлен мастеру!", reply_markup=main_menu)
    await state.clear()
    await callback.answer()

# ========== МОДЕЛЬ С ЛОГО И 7 ФОТО (с поддержкой альбомов) ==========
@dp.callback_query(lambda c: c.data == "choose_model_7photo")
async def choose_model_7photo(callback: types.CallbackQuery, state: FSMContext):
    await delete_unwanted_photos(callback.from_user.id, keep_index=2)
    await callback.message.delete()
    await state.set_state(OrderModel7Photo.waiting_for_light)
    await state.update_data(ref_photos=[])
    await callback.message.answer(
        "💡 Выбери подсветку для картины:",
        reply_markup=light_kb
    )
    await callback.answer()

@dp.message(OrderModel7Photo.waiting_for_light)
async def get_light_7photo(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if message.text not in ["💡 Теплый белый", "❄️ Холодный белый", "🌈 RGB", "🚫 Без подсветки"]:
        await message.answer("Пожалуйста, выбери подсветку из кнопок")
        return
    await state.update_data(light=message.text)
    await state.set_state(OrderModel7Photo.waiting_for_ref_photos)
    await message.answer(
        "📸 Шаг 1 из 2: Пришли 4 фото авто\n\nЭто нужно чтобы мы могли максимально точно сделать модельку твоего авто",
        reply_markup=back_button
    )

@dp.message(OrderModel7Photo.waiting_for_ref_photos)
async def get_ref_photos_7(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if not message.photo:
        await message.answer("Пожалуйста, пришли фото")
        return
    
    data = await state.get_data()
    existing_photos = data.get('ref_photos', []).copy()
    target = 4
    
    if message.media_group_id:
        media_group_id = message.media_group_id
        
        if media_group_id not in temp_albums:
            temp_albums[media_group_id] = {
                "photos": [],
                "user_id": message.from_user.id,
                "target": target,
                "step": "ref"
            }
        
        temp_albums[media_group_id]["photos"].append(message.photo[-1].file_id)
        await asyncio.sleep(1.5)
        
        if media_group_id in temp_albums:
            album_data = temp_albums.pop(media_group_id)
            new_photos = list(dict.fromkeys(album_data["photos"]))
        else:
            return
    else:
        new_photos = [message.photo[-1].file_id]
    
    all_photos = existing_photos + new_photos
    all_photos = list(dict.fromkeys(all_photos))
    
    await state.update_data(ref_photos=all_photos)
    current = len(all_photos)
    
    if current >= target:
        all_photos = all_photos[:target]
        await state.update_data(ref_photos=all_photos)
        await state.set_state(OrderModel7Photo.waiting_for_final_photos)
        await state.update_data(final_photos=[])
        await message.answer(f"✅ Получено {target} референсных фото!\n\n🖼️ Шаг 2 из 2: Теперь пришли 7 фотографий для картины\n\nКакую фотографию куда вставить обсуждается с менеджером", reply_markup=back_button)
    else:
        await message.answer(f"✅ Получено {current}/{target} фото. Пришли ещё {target - current}.")

@dp.message(OrderModel7Photo.waiting_for_final_photos)
async def get_final_photos_7(message: types.Message, state: FSMContext):
    if message.text == "🔙 Назад / В начало":
        await back_to_main(message, state)
        return
    if not message.photo:
        await message.answer("Пожалуйста, пришли фото")
        return
    
    data = await state.get_data()
    existing_photos = data.get('final_photos', []).copy()
    target = 7
    
    if message.media_group_id:
        media_group_id = message.media_group_id
        
        if media_group_id not in temp_albums:
            temp_albums[media_group_id] = {
                "photos": [],
                "user_id": message.from_user.id,
                "target": target,
                "step": "final"
            }
        
        temp_albums[media_group_id]["photos"].append(message.photo[-1].file_id)
        await asyncio.sleep(1.5)
        
        if media_group_id in temp_albums:
            album_data = temp_albums.pop(media_group_id)
            new_photos = list(dict.fromkeys(album_data["photos"]))
        else:
            return
    else:
        new_photos = [message.photo[-1].file_id]
    
    all_photos = existing_photos + new_photos
    all_photos = list(dict.fromkeys(all_photos))
    
    await state.update_data(final_photos=all_photos)
    current = len(all_photos)
    
    if current >= target:
        all_photos = all_photos[:target]
        await state.update_data(final_photos=all_photos)
        await state.set_state(OrderModel7Photo.waiting_for_confirm)
        
        confirm_text = f"📋 ПРОВЕРЬ ЗАКАЗ (Модель с лого и 7 фото)\n\n💡 Подсветка: {data.get('light', '—')}\n\n📸 Референсные фото: {len(data.get('ref_photos', []))} шт.\n🖼️ Фото для картины: {len(all_photos)} шт.\n\n✅ Всё верно?\n❌ Или начать сначала?"
        
        confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="✅ Да, отправить заказ", callback_data="confirm_7photo_send")],
            [InlineKeyboardButton(text="🔄 Переделать сначала", callback_data="confirm_cancel")]
        ])
        
        ref_photos = data.get('ref_photos', [])
        if ref_photos:
            ref_media = [types.InputMediaPhoto(media=pid, caption="📸 Референс") for pid in ref_photos]
            await message.answer_media_group(ref_media)
        
        final_media = [types.InputMediaPhoto(media=pid, caption="🖼️ Для картины") for pid in all_photos]
        if final_media:
            await message.answer_media_group(final_media)
        
        await message.answer(confirm_text, reply_markup=confirm_kb)
    else:
        await message.answer(f"✅ Получено {current}/{target} фото. Пришли ещё {target - current}.")

@dp.callback_query(lambda c: c.data == "confirm_7photo_send")
async def confirm_7photo_send(callback: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    username = callback.from_user.username or callback.from_user.first_name
    
    order_text = f"🔥 НОВЫЙ ЗАКАЗ (Модель с лого и 7 фото)\n\n👤 Клиент: @{username}\n\n💡 Подсветка: {data.get('light', '—')}\n\n📸 Референсы: {len(data.get('ref_photos', []))} шт.\n🖼️ 7 фото: {len(data.get('final_photos', []))} шт."
    
    await bot.send_message(CHANNEL_ID, order_text)
    
    for pid in data.get('ref_photos', []):
        await bot.send_photo(CHANNEL_ID, pid)
    
    for pid in data.get('final_photos', []):
        await bot.send_photo(CHANNEL_ID, pid)
    
    await callback.message.delete()
    await callback.message.answer("✅ Заказ отправлен мастеру!", reply_markup=main_menu)
    await state.clear()
    await callback.answer()

@dp.callback_query(lambda c: c.data == "back_to_menu")
async def back_menu(callback: types.CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    if user_id in user_data_store:
        for mid in user_data_store[user_id].get("example_message_ids", []):
            try:
                await bot.delete_message(user_id, mid)
            except:
                pass
        del user_data_store[user_id]
    await callback.message.delete()
    await state.clear()
    await callback.message.answer("🏠 Главное меню", reply_markup=main_menu)
    await callback.answer()

async def main():
    print("🤖 Бот TAIRO запущен!")
    print(f"✅ Заказы отправляются в канал: {CHANNEL_ID}")
    print("✅ Поддерживается отправка нескольких фото в одном сообщении (альбомы)")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
