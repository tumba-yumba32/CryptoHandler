import asyncio
from aiogram import Bot,Dispatcher
from apps.crypto_handlers import router



TOKEN = "7796824593:AAEdnoZVhP-NI2kePIDQzx79L4c8eWxZBdA"
async def main():
    bot = Bot(token=TOKEN)
    dispatcher = Dispatcher()
    dispatcher.include_router(router)
    await dispatcher.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot has been end work")
























