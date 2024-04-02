from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

select_language = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="RU"
        )
    ],
    [
        KeyboardButton(
            text="EN"
        )
    ]
])

select_time_zone_ru = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Мск"
        )
    ],
    [
        KeyboardButton(
            text="Мск+1"
        )
    ],
    [
        KeyboardButton(
            text="Мск-1"
        )
    ]
])

select_time_zone_en = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(
            text="Msc"
        )
    ],
    [
        KeyboardButton(
            text="Msc+1"
        )
    ],
    [
        KeyboardButton(
            text="Msc-1"
        )
    ]
])