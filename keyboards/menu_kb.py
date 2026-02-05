from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="📖 Подробнее",
                callback_data="about_company"
            )
        ],
        [
            InlineKeyboardButton(
                text="🤖 Узнать",
                callback_data="products"
            )
        ]
    ]
)
