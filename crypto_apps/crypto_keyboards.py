from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

funct_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text = "Crypto course")],
                                               [KeyboardButton(text = "About crypto")],
                                               [KeyboardButton(text ="Bot info")]],
                                     resize_keyboard=True,input_field_placeholder="Choose menu button")

crypto_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Bitcoin",callback_data = "BTCRUB")],
    [InlineKeyboardButton(text="Doge",callback_data = "DOGERUB")],
    [InlineKeyboardButton(text="XRP",callback_data = "XRPRUB")],
    [InlineKeyboardButton(text="Binance Coin",callback_data = "BNBRUB")],
    [InlineKeyboardButton(text="Cardano",callback_data = "ADARUB")]
])

info_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Bitcoin",callback_data = "BTCinfo")],
    [InlineKeyboardButton(text="Ethereum",callback_data = "ETCinfo")],
    [InlineKeyboardButton(text="Doge",callback_data = "DOGEinfo")],
    [InlineKeyboardButton(text="XRP",callback_data = "XRPinfo")],
    [InlineKeyboardButton(text="Binance Coin",callback_data = "BNBinfo")],
    [InlineKeyboardButton(text="Cardano",callback_data = "ADAinfo")]
])






























