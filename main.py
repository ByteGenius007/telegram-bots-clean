import asyncio
from bots.marat_bot import dp as dp_marat, bot as bot_marat
from bots.admin_bot import dp as dp_admin, bot as bot_admin
import os
import sys
async def main():
    if os.getenv("BOT_ENABLED") == "false":
        print("Bot disabled")
        sys.exit()

    # запускаем оба бота параллельно
    await asyncio.gather(
        dp_marat.start_polling(bot_marat),
        dp_admin.start_polling(bot_admin)
    )

if __name__ == "__main__":
    asyncio.run(main())
