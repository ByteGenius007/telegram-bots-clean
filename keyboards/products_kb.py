from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_products_keyboard(products):
    keyboard = []

    for product in products:
        # Основная кнопка продукта
        buttons = [
            InlineKeyboardButton(
                text=product["button"],
                callback_data=f"product:{product['id']}"
            )
        ]

        # Если есть ссылка на видео, добавляем отдельную кнопку
        if "video_url" in product:
            buttons.append(
                InlineKeyboardButton(
                    text="👈📺 Посмотреть видео",
                    url=product["video_url"]
                )
            )

        # Добавляем строку с кнопками для продукта
        keyboard.append(buttons)

    # Кнопка "Назад к меню"
    keyboard.append([
        InlineKeyboardButton(
            text="⬅ Назад к меню",
            callback_data="back_to_products_menu"
        )
    ])

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
