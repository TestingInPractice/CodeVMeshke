print("Ваш вес (кг):")
weight = float(input())
print("Ваш рост (м):")
height = float(input())

bmi = weight / (height ** 2)

if bmi < 18.5:
    status = "Недостаточный вес ❌"
elif 18.5 <= bmi < 25:
    status = "Норма ✅"
else:
    status = "Избыточный вес ⚠️"

print(f"ИМТ: {bmi:.1f} — {status}")
