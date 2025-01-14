def main(n):
    """
    n uch xonali son berilgan. Raqamlar yig'indisi raqamlar ko'paymasidan kichikligini tekshiring. Agar kichik bo'lsa True aks holatda False.
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    """
    n = abs(n)
    a1 = n // 100
    a2 = (n // 10) % 10
    a3 = n % 10
    
    x1 = a1 + a2 + a3
    x2 = a3 * a2 * a1 

    return x1 < x2
