def main(a):
    """
    Berilgan ikkita raqamli a sonida "Sonning barcha raqamlarining yig'indisi toq" ekanligini tekshirish.
    Argumentlar:
        a(int): a parametri (ikkita raqamli son)
    Qaytaradi:
        bool: javob (True yoki False)
    """
    # Raqamlarning yig'indisi toqmi?
    a = abs(a)
    
    x1 = a // 10
    x2 = a % 10
    t = x1 + x2
    return t % 2 == 1
