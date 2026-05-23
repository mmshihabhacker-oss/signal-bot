import asyncio
import random
from telegram import Bot

TOKEN = "8870951088:AAEKS7GU_fr5sRQ7Qk6LH0q3L80wFx3DEUQ"
CHAT_ID = "@XPERSONALSIGNALBOT"

pairs = [

    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "AUD/USD",
    "USD/CAD",
    "USD/CHF",
    "NZD/USD",

    "EUR/GBP",
    "EUR/JPY",
    "EUR/AUD",
    "EUR/CAD",
    "EUR/CHF",
    "GBP/JPY",
    "GBP/AUD",
    "GBP/CAD",
    "GBP/CHF",

    "AUD/JPY",
    "AUD/CAD",
    "AUD/CHF",

    "CAD/JPY",
    "CHF/JPY",

    "NZD/JPY",
    "NZD/CAD",
    "NZD/CHF",

    "EUR/NZD",
    "GBP/NZD",
    "AUD/NZD",

    "USD/MXN",
    "USD/SGD",
    "USD/TRY",
    "USD/ZAR",

    "EUR/TRY",
    "GBP/SGD",
    "AUD/SGD"

]

signals = [
    "CALL 📈",
    "PUT 📉"
]

times = [
    "M1",
    "M5"
]

async def main():

    bot = Bot(token=TOKEN)

    while True:

        pair = random.choice(pairs)
        signal = random.choice(signals)
        timeframe = random.choice(times)

        message = f"""
🚨 SIGNAL ALERT 🚨

📊 Pair: {pair}
⏰ Timeframe: {timeframe}
🎯 Signal: {signal}

🔥 Trade Carefully
"""

        await bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

        print("Signal Sent ✅")

        await asyncio.sleep(60)

asyncio.run(main())
