def convert_grams_to_cups(grams, product):
    density = {
        "мука": 125,
        "сахар": 200,
        "вода": 250
    }
    cups = grams / density.get(product, 200)
    print(f"{grams} г ≈ {cups:.1f} стаканов ({product})")

convert_grams_to_cups(320, "мука")
