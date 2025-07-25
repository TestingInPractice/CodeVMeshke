print("Введите сумму в USD:")
usd_amount = float(input())

exchange_rate = 90.5  # Начальный курс RUB/USD
rub_amount = usd_amount * exchange_rate
print(f"{usd_amount} USD = {rub_amount} RUB (курс {exchange_rate})")

exchange_rate = 95.0  # Новый курс
rub_amount = usd_amount * exchange_rate
print(f"{usd_amount} USD = {rub_amount} RUB (курс {exchange_rate})")
