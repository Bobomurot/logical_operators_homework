def main(a):
    """
    Berilgan besh xonali a butun soni, quyidagi holatni tekshiring: "Sonning barcha raqamlari oshib boruvchi tartibda."
    Args:
        a(int): parametr a
    Returns:
        bool: javob
    """
    a = abs(a)
    x1 = a // 10000
    x2 = (a // 1000) % 10
    x3 = (a // 100) % 10
    x4 = (a // 10) % 10
    x5 = a % 10
    return x1 < x2 < x3 < x4 < x5
