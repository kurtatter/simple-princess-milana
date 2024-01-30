from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Афиша [с картинками]")
        ],
        [
            KeyboardButton(text="Афиша [список]")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    input_field_placeholder="Нажмите на кнопку Афиша",
    selective=True
)
