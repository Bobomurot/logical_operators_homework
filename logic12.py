def main(a):
    """
    Berilgan ikkita raqamli a sonida "Sonning barcha raqamlari bir xil" ekanligini tekshirish.
    Argumentlar:
        a(int): a parametri (ikkita raqamli son)
    Qaytaradi:
        bool: javob (True yoki False)
    """
    a = abs(a)
    x1 = a // 10
    x2 = a % 10
    
    return x1 == x2
