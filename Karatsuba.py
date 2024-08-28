
def karatsuba(x : str, y : str) -> int:
    n = len(x)
    ny = len(y)
    # Checking if lengths differ and making them equal if so
    # Add zeros to the front of the string to make them equal
    if (ny > n):
        dif = ny - n
        zero = '0'
        for _ in range(dif):
            x = zero + x
        n = ny
    # Checking if lengths differ and making them equal if so
    # Add zeros to the front of the string to make them equal
    elif (n > ny):
        dif = n - ny
        zero = '0'
        for _ in range(dif):
            y = zero + y
    # Checking if length of numbers is odd, which doesn't work for this algorithm
    if n != 1 and (n % 2 == 1):
            zero = '0'
            y = zero + y
            x = zero + x
            n += 1
    # Base case
    if n == 1 and ny == 1:
        return int(x) * int(y)
    # Recursive case
    else:
        half = n // 2
        # Split the numbers
        a, b = (x[:half], x[half:])
        c, d = (y[:half], y[half:])
        # Recursively calculate a*c and b*d
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        p = str(int(a) + int(b))
        q = str(int(c) + int(d))
        # Recursively calculate p*q to get adbc later.
        pq = karatsuba(p, q)
        # Since (a+b)(c+d) = ac + bd + ad + bc, we get rid of ac+bd because we already have those values.
        adbc = pq - ac - bd
        return int((10**n) * ac + (10**(half)) * adbc + bd)


def main():
    x = '3141592653589793238462643383279502884197169399375105820974944592'
    y = '2718281828459045235360287471352662497757247093699959574966967627'
    print(karatsuba(x, y))
    intxy = int(x) * int(y)
    print(intxy)

if __name__ == '__main__':
    main()
