from aiogram import F, Router
from aiogram.types import Message,CallbackQuery
from aiogram.filters import CommandStart, Command

from crypto_apps import crypto_keyboards as kb
from crypto_apps.info import crypto_information


import requests
import json


router = Router()


CRYPTO_NAME_TO_TICKER = {
    "Bitcoin": "BTCRUB",
    "Ethereum": "ETHUSDT",
    "Doge": "DOGERUB",
    "XRP":"XRPRUB",
    "Binance coin":"BNBRUB",
    "Corando": "ADARUB"
}


@router.message(CommandStart())
async def command_start(message: Message):
    await message.answer("Здарова!", reply_markup=kb.funct_keyboard)


@router.message(F.text == "Crypto course")
async def choose_crypto_button(message: Message):
    await message.answer("Доступные курсы криптовалют в рублях:",reply_markup=kb.crypto_keyboard)

@router.callback_query(F.data.in_(CRYPTO_NAME_TO_TICKER.values()))
async def crypto_selection(callback: CallbackQuery):
    await callback.answer("looking for information...")
    ticker = callback.data
    name = None

    for key, value in CRYPTO_NAME_TO_TICKER.items():
        if ticker == value:
            name = key
            break

    response = requests.get(url = "https://api.binance.com/api/v3/ticker/price", params = {"symbol" : ticker})
    price = response.json()["price"]

    await callback.message.answer(f"Price of {name} for now is: {price} ₽")

@router.message(F.text == "About crypto")
async def crypto_info(message: Message):
    await message.answer("What crypto do you want to know about?",reply_markup = kb.info_keyboard)

@router.callback_query(F.data.in_(crypto_information.keys()))
async def get_info(callback: CallbackQuery):
    crypto = callback.data
    await callback.answer("looking for information...")
    await callback.message.answer(crypto_information[crypto])


@router.message(F.text == "Bot info")
async def bit_info_get(message: Message):
    await message.answer("CДЕЛАНО АРТЁМОМ ВЕЛИКИМ НА api binance \n ZZZZZZZZZZZZZZZZZZZOOOOOOOOOOOOOOOOOOOVVVVVVVVVV \n GOOOOOOOOOOOOOOIIIIIIIIIIIIIIDAAAAAAAAAAAAAAAAA")


















