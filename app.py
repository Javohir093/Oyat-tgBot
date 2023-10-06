import logging
import asyncio
import sys
from button import files
from states import Oyatst
from aiogram.filters import CommandStart
from aiogram import Dispatcher, types, Bot,F
from config import BOT_TOKEN
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from button import get_name_markup

dp=Dispatcher()

chapt_numb=[]

@dp.message(CommandStart())
async def get_start(message:types.Message, state:FSMContext):
    await message.answer(text="Suralardan birini tanlang!",reply_markup=get_name_markup())
    await state.set_state(Oyatst.Oyat)


@dp.message(F.text, Oyatst.Oyat)
async def get_chapters(message:types.Message, state:FSMContext):
    mesg=str(message.text)
    a=mesg.split(".")
    numb=int(a[0])
    numb_ver=0
    await state.set_data({"chap_num": numb})
    for ver in  files["quran"]:
        if ver["chapter"] == numb:
            numb_ver+=1
    await message.answer(text=f"Oyat raqamini kirgizing, jami {numb_ver} ta oyat bor")
    await state.set_state(Oyatst.Verse)



@dp.message(F.text, Oyatst.Verse)
async def get_verses(message:types.Message, state:FSMContext):
    mesg=int(message.text)
    data = await state.get_data()
    chap_num = data.get("chap_num")
    for ver in  files["quran"]:
        if ver["chapter"] == chap_num and ver["verse"] == mesg:
            a=ver["text"]
            await message.answer(text=f"Sizga kerak bo'lgan o'yat\n\n{a}")
    await state.set_state(Oyatst.Oyat)



async def main():
    bot=Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__=="__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except Exception as error:
        print(error)