def main(a):
    """
    Berilgan ikkita raqamli a sonida "Sonning barcha raqamlarining yig'indisi juft" ekanligini tekshirish.
    Argumentlar:
        a(int): a parametri (ikkita raqamli son)
    Qaytaradi:
        bool: javob (True yoki False)
    """
    a = abs(a)
    
    x1 = a // 10
    x2 = a % 10
    t = x1 + x2
    return t % 2 == 0

    # Raqamlarning yig'indisi juftmi?
    return 
x = main(44)
print(x)