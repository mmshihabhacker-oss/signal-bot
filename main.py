import os
import time
import random
from telegram import Bot

# =========================
# SHIHAB SIGNAL BOT
# =========================

BOT_TOKEN = "8870951088:AAEKS7GU_fr5sRQ7Qk6LH0q3L80wFx3DEUQ"
CHAT_ID = "-1003334645126"

bot = Bot(token=BOT_TOKEN)

# =========================
# REAL MARKET PAIRS
# =========================

pairs = [
    "EURUSD",
    "GBPUSD",
    "USDJPY",
    "AUDUSD",
    "USDCAD",
    "USDCHF",
    "NZDUSD",
    "EURJPY",
    "GBPJPY",
    "EURGBP",
    "AUDJPY",
    "CADJPY",
    "CHFJPY",
    "EURAUD",
    "GBPAUD",
    "GBPCAD",
    "GBPCHF",
    "AUDCAD",
    "AUDCHF",
    "NZDJPY",
    "NZDCHF",
    "NZDCAD",
    "EURCAD",
    "EURCHF",
    "USDMXN",
    "USDTRY",
    "USDZAR",
    "USDSGD",
    "USDNOK",
    "USDSEK"
]

signals = ["BUY", "SELL"]

# =========================
# SEND SIGNAL
# =========================

def send_signal():

    pair = random.choice(pairs)
    signal = random.choice(signals)

    entry = round(random.uniform(1.10000, 99.99999), 5)

    current_time = time.strftime("%H:%M")

    timeframe = random.choice(["1 Minute", "5 Minute"])

    if signal == "BUY":
        icon = "🟢 BUY"
    else:
        icon = "🔴 SELL"

    message = f"""
SHIHAB SIGNAL BOT _ 90%

📊 {pair}

⏰ Time: {current_time}
📈 {timeframe}

🎯 Entry: {entry}
{icon}

⏩ If loss 1 MTG
"""

    bot.send_message(
        chat_id=CHAT_ID,
        text=message
    )

    # WAIT RESULT
    if timeframe == "1 Minute":
        time.sleep(60)
    else:
        time.sleep(300)

    result = random.choice(["WIN", "LOSS"])

    # =========================
    # RESULT MESSAGE
    # =========================

    if result == "WIN":

        result_message = f"""
📊 {pair}

⏰ Time: {current_time}
📈 {timeframe}

🎯 Entry: {entry}
{icon}

✅ WIN ✅
"""

    else:

        result_message = f"""
📊 {pair}

⏰ Time: {current_time}
📈 {timeframe}

🎯 Entry: {entry}
{icon}

❌ MTG LOSS
"""

    bot.send_message(
        chat_id=CHAT_ID,
        text=result_message
    )

# =========================
# RUN BOT
# =========================

while True:

    try:

        send_signal()

        # CHECK EVERY 5 SECOND
        time.sleep(5)

    except Exception as e:

        print(e)

        time.sleep(10)
