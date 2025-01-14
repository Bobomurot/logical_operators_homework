def main(a):
    """
    Berilgan uchta raqamli a sonida "Sonning barcha raqamlarining yig'indisi toq" ekanligini tekshirish.
    Argumentlar:
        a(int): a parametri (uchta raqamli son)
    Qaytaradi:
        bool: javob (True yoki False)
    """
    
    # Raqamlarning yig'indisi toqmi?
    a = abs(a)
    x1 = a // 100
    x2 = a // 10
    x3 = a % 10
    t = x1 + x2 + x3
    return t % 2 == 1
x = main(335)
print(x)