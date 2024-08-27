
def karatsuba(x : int, y : int) -> int:
    n = len(str(x))
    ny = len(str(y))
    if (n == 1 and ny > 1) or (ny == 1 and n > 1):
        ...
    if n == 1 and ny == 1:
        return x * y
    else:
        a, b = (int(str(x)[:n//2]), int(str(x)[n//2:]))
        c, d = (int(str(y)[:n//2]), int(str(y)[n//2:]))
        print(f"{a}:{b} {c}:{d}")
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        p = a + b
        q = c + d
        pq = karatsuba(p, q)
        adbc = pq - ac - bd
        return int((10**n) * ac + (10**(n/2)) * adbc + bd)


def main():
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627

    karatsuba(x, y)

if __name__ == '__main__':
    main()
