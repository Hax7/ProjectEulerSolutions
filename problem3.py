def larges_prime_factor(x):
    n = 2
    while n * n <= x:
        if x % n == 0:
            x /= n
        else:
            n += 1
    return x
