import math
from turtle import forward, left, up, down


# 1. Drawing a rectangle with diagonals

def crossed_rectangle(width, height):
    pif = math.hypot(height, width)
    argt = math.atan(height / width) * 180 / math.pi
    for i in range(2):
        left(90)
        forward(height)
        left(90)
        forward(width)
    left(180 - argt)
    forward(pif)
    up()
    left(90 + argt)
    forward(height)
    down()
    left(90 + argt)
    forward(pif)


# 2. Calculating the sum of the first "count" numbers that are divisible by "div" and not divisible by "nondiv"

def sum_elements_dn(div, nondiv, count):
    x = div
    y = 0
    while 0 < count:
        if x % div == 0 and x % nondiv != 0:
            y += x
            count -= 1
            x += div
        else:
            x += div
    return y


# 3. Finding the "index" unique prime divisor of a number "num"

def nth_unique_smallest_prime_divisor(num, index):
    n = num
    d = 2
    actual = fin_ind = 0
    while d * d <= n:
        if n % d == 0:
            if d != actual:
                fin_ind += 1
                if fin_ind == index:
                    return d
                actual = d
            n //= d
        else:
            d += 1
    if n > 1:
        fin_ind += 1
        if fin_ind == index and n > actual:
            return n
        return None


def main():
    # you have to check the output of crossed_rectangle yourself
    assert sum_elements_dn(3, 2, 7) == 147
    assert sum_elements_dn(6, 4, 5) == 150
    assert sum_elements_dn(10, 6, 11) == 910

    assert nth_unique_smallest_prime_divisor(12, 2) == 3
    assert nth_unique_smallest_prime_divisor(42350, 2) == 5
    assert nth_unique_smallest_prime_divisor(42350, 3) == 7
    assert nth_unique_smallest_prime_divisor(42350, 4) == 11
    assert nth_unique_smallest_prime_divisor(42350, 5) is None


if __name__ == '__main__':
    main()
