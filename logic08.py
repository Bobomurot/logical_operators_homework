def main(a, b):
    """
    Ikki butun son a va b berilgan, "a va b ning kamida bittasi juft" degan gapni tekshirish.
    Argumentlar:
        a(int): a parametri
        b(int): b parametri
    Qaytaradi:
        bool: javob (True yoki False)
    """
    return a % 2 == 0 or b % 2 == 0
x = main(4, 7)
print(x)

