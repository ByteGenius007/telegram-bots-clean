import asyncio
import json
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, KeyboardButton, ReplyKeyboardMarkup, InputMediaPhoto
from aiogram import F

from config import BOTS
from keyboards.menu_kb import main_menu_kb
from keyboards.products_kb import get_products_keyboard
from handlers.ai_handler import ask_openai


from aiogram.types import Message

from database import is_subscriber
from database import add_subscriber

bot = Bot(token=BOTS["marat"])
dp = Dispatcher()

# Кнопка запроса номера телефона для проверки, что человек
phone_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Я не робот (отправить номер телефона)", request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

# Функция отправки основного приветствия и меню
async def send_start_message(message: types.Message):
    photo = FSInputFile("media/photos/flavon.jpg")
    user_name = message.from_user.first_name or "друг"
    
    # приветствие
    await message.answer_photo(
        photo=photo,
        caption=(f"Приветствую, {user_name}! 👋\n\n"
        )
    )

    # про компанию
    await message.answer(
    """Flavon — это венгерская сила, которая уже более 21 года меняет жизни миллионов людей по всему миру.
Представь: компания с собственным полным циклом производства в Европе (Венгрия), строжайшим контролем качества, сырьём от лучших поставщиков Германии, Италии, Франции. Никаких компромиссов. Только премиум-ингредиенты, инновационная гель-консистенция, которая доставляет в клетки максимум биофлавоноидов, антиоксидантов и фитонутриентов из 50+ видов фруктов, ягод и овощей.
Продукты Flavon — это не просто БАДы.
Это клеточное питание будущего:
рекордные показатели ORAC (до 188 000+ единиц в суточной дозе!)
мощная защита от свободных радикалов
реальная поддержка при высоких нагрузках, восстановлении, возрастных изменениях
линейка для детей, взрослых, спортсменов, премиум-сегмент Peak
А теперь самое интересное для партнёров:
Маркетинг-план — один из самых щедрых в индустрии — до 65% идёт в сеть.
Комиссия с первой коробки, равные шансы для всех с первого дня, стабильная структура, которая не менялась годами.
В 2025 году Flavon мощно заходит в Казахстан и СНГ — рынок открывается прямо сейчас.
Это не «ещё одна компания». Это момент, когда лидеры забирают целые регионы и строят команды на старте взрывного роста.
Если ты хочешь:
работать с реально работающим продуктом, который люди кушают каждый день и рекомендуют
зарабатывать по-европейски щедро и без постоянных перезапусков плана
войти в проект раньше 99% рынка СНГ
Flavon — это твой билет в новую лигу.
Готов стать частью европейского премиум-бренда, который меняет здоровье и доходы людей одновременно?
Напиши мне прямо сейчас — покажем цифры, продукт и как войти на самых выгодных условиях.
Это не просто бизнес. Это новый уровень."""
        )


    

    # меню
    await message.answer(
        "Выбери, что хочешь узнать дальше 👇",
        reply_markup=main_menu_kb
    )

# Старт бота
@dp.message(CommandStart())
async def start(message: types.Message):
    user_id = message.from_user.id

    if not await is_subscriber(user_id):
        await message.answer(
            "Привет! Перед тем как начать, подтвердите, что вы человек 👇",
            reply_markup=phone_kb
        )
        return

    await send_start_message(message)


# Обработка контакта (проверка "не робот")

@dp.message(F.contact)
async def phone_confirm(message: types.Message):
    user_id = message.from_user.id

    await add_subscriber(user_id)
    await send_start_message(message)


@dp.callback_query(F.data == "about_company")
async def about_company(callback: types.CallbackQuery):
    video = FSInputFile("media/videos/intro.mp4")
    await callback.answer()

    await callback.message.answer(
        """Flavon — это венгерская сила, которая уже более 21 года меняет жизни миллионов людей по всему миру.
Представь: компания с собственным полным циклом производства в Европе (Венгрия), строжайшим контролем качества, сырьём от лучших поставщиков Германии, Италии, Франции. Никаких компромиссов. Только премиум-ингредиенты, инновационная гель-консистенция, которая доставляет в клетки максимум биофлавоноидов, антиоксидантов и фитонутриентов из 50+ видов фруктов, ягод и овощей.
Продукты Flavon — это не просто БАДы.
Это клеточное питание будущего:
рекордные показатели ORAC (до 188 000+ единиц в суточной дозе!)
мощная защита от свободных радикалов
реальная поддержка при высоких нагрузках, восстановлении, возрастных изменениях
линейка для детей, взрослых, спортсменов, премиум-сегмент Peak
А теперь самое интересное для партнёров:
Маркетинг-план — один из самых щедрых в индустрии — до 65% идёт в сеть.
Комиссия с первой коробки, равные шансы для всех с первого дня, стабильная структура, которая не менялась годами.
В 2025 году Flavon мощно заходит в Казахстан и СНГ — рынок открывается прямо сейчас.
Это не «ещё одна компания». Это момент, когда лидеры забирают целые регионы и строят команды на старте взрывного роста.
Если ты хочешь:
работать с реально работающим продуктом, который люди кушают каждый день и рекомендуют
зарабатывать по-европейски щедро и без постоянных перезапусков плана
войти в проект раньше 99% рынка СНГ
Flavon — это твой билет в новую лигу.
Готов стать частью европейского премиум-бренда, который меняет здоровье и доходы людей одновременно?
Напиши мне прямо сейчас — покажем цифры, продукт и как войти на самых выгодных условиях.
Это не просто бизнес. Это новый уровень."""
    , parse_mode="Markdown")

    # видео
    await callback.message.answer_video(
        video=video,
        caption="Короткое видео"
    )

    # меню
    await callback.message.answer(
        "Выбери, что хочешь узнать дальше 👇",
        reply_markup=main_menu_kb
    )


    


@dp.callback_query(F.data == "products")
async def products(callback: types.CallbackQuery):
    
    with open("data/products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    keyboard = get_products_keyboard(products)
    # Редактируем текст (текстное сообщение -> список кнопок)
    await callback.message.edit_text(
        "Выбери 👇",
        reply_markup=keyboard
    )
    await callback.answer()



@dp.callback_query(F.data.startswith("product:"))
async def open_product(callback: types.CallbackQuery):
    product_id = callback.data.split(":")[1]

    with open("data/products.json", "r", encoding="utf-8") as f:
        products = json.load(f)

    product = next(p for p in products if p["id"] == product_id)

    await callback.message.edit_media(
        media=InputMediaPhoto(
            media=FSInputFile(product["photo"]),
            caption=f"<b>{product['name']}</b>\n\n{product['description']}",
            parse_mode="HTML"
        ),
        reply_markup=get_products_keyboard(products)
    )

    await callback.answer()


@dp.callback_query(F.data == "back_to_products_menu")
async def back_to_products(callback: types.CallbackQuery):

    await callback.message.delete()

    # меню
    await callback.message.answer(
        "Выбери, что хочешь узнать дальше 👇",
        reply_markup=main_menu_kb
    )
    await callback.answer()



@dp.message()
async def messages_router(message: types.Message):
    text = message.text
    if not text:
        return

    # --- КНОПКИ ГЛАВНОГО МЕНЮ (ИИ НЕ РАБОТАЕТ) ---
    menu_buttons = [
        "lol"
    ]

    if text in menu_buttons or text.startswith("/"):
        return

    # --- ПРОВЕРКА ТОВАРОВ (ИИ НЕ ЛЕЗЕТ) ---
    try:
        with open("data/products.json", "r", encoding="utf-8") as f:
            products = json.load(f)

        for product in products:
            if text == product["button"]:
                photo = FSInputFile(product["photo"])
                await message.answer_photo(
                    photo=photo,
                    caption=f"{product['name']}\n\n{product['description']}",
                    reply_markup=main_menu_kb  # меню ВСЕГДА видно
                )
                return
    except Exception as e:
        print("Ошибка при проверке товаров:", e)

    # --- ЕСЛИ ЭТО ОБЫЧНЫЙ ТЕКСТ → ИИ ---
    try:
        await message.answer("🤖 Думаю...")
        answer = ask_openai(message.from_user.id, text)
        await message.answer(answer, reply_markup=main_menu_kb)
    except Exception as e:
        print("Ошибка OpenAI:", e)
        await message.answer("⚠️ Сейчас не могу ответить, попробуй позже 🙏", reply_markup=main_menu_kb)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    print("TOKEN:", BOTS["marat"])
