def main(x):
    """
    Berilgan ikki xonali x butun soni, uning polindrom ekanligini tekshirib, javob qaytaring.
    Polindrom son, orqaga qarab o'qilganda ham bir xil bo'ladi.

    Args:
        x(int): parametr x
    Returns:
        bool: javob
    """
    x = int(x)
    a1 = x // 10
    a2 = x % 10
    return a1 == a2
