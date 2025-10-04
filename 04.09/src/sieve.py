from math import isqrt


def sieve(n: int) -> list[int]:
    """
    Алгоритм генерации решета Эратосфена

    Мы инициализируем решето размером (n - 1) // 2, так как больше оно не может быть
    Затем проходимся по всем нечётным числам до корня из n
        (i является индексом, в num содержится соответствующее простое число)
    Затем мы вычёркиваем все невычеркнутые кратные числа для num, которые уже не являются простыми

    В конце мы по оставшимся индексам собираем оставшиеся нечётные числа, которые являются простыми

    Args:
        n (int): число, до которого нужно генерировать решето (включительно)

    Returns:
        list[int]: список простых чисел до n
    """

    if n < 2:
        return []
    if n == 2:
        return [2]

    num_count = (n - 1) // 2
    is_prime = [True for _ in range(num_count)]

    for i in range((isqrt(n) - 1) // 2 + 1):
        if is_prime[i]:
            num = 2 * i + 3
            for j in range((num**2 - 3) // 2, num_count, num):
                is_prime[j] = False

    return [2] + [2 * i + 3 for i, prime in enumerate(is_prime) if prime]


n = int(input())
print(sieve(n))
