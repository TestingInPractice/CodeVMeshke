# TODO: Реализуйте функцию convert_grams_to_cups и вызовите её с параметрами 320 и "мука"
def convert_grams_to_cups(grams, product):
    density = {
        "мука": 160,
        "сахар": 200,
        "вода": 250
    }
    # Ваша формула здесь
    cups = ...
    print(f"{grams} г ≈ {cups:.1f} стаканов ({product})")

convert_grams_to_cups(320, "мука")
