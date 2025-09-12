def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """_summary_

    Реализация расширенного алгоритма Евклида

    Args:
        a (int): первое число
        b (int): второе число

    Returns:
        tuple[int, int, int]: кортеж, содержащий НОД на первой позиции, коэффициенты перед первым и вторым числом на 2 и 3 позиции соответственно
    """

    if b == 0:
        return (a, 1, 0)

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return (gcd, x, y)
