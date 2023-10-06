import json
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


home_info="E:/bekent dev/Oyat-tgBot/info.json"
home_uzb="E:/bekent dev/Oyat-tgBot/uzb-muhammadsodikmu.json"


with open(f"{home_info}", "r") as info1:
    info=json.load(info1)
with open(f"{home_uzb}", "r", encoding="utf-8") as uzb1:
    files = json.load(uzb1)


def get_name_markup() -> ReplyKeyboardMarkup:
    kb=ReplyKeyboardBuilder()
    for i in range(0,114):
        numb=info["chapters"][i]["chapter"]
        name=info["chapters"][i]["name"]
        kb.add(KeyboardButton(text=f"{numb}.{name}"))
    kb.adjust(4)
    return kb.as_markup(resize_keyboard=True)




