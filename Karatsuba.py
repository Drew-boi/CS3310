import time
lookup = {}
for i in range(0 , 10):
    for j in range(0, 10):
        lookup[(str(i), str(j))] = i * j

def karatsuba(x : str, y : str) -> int:
    # Make x and y equal lengths
    n = max(len(x), len(y))
    x = x.zfill(n)
    y = y.zfill(n)
    # Base case
    if n == 1:
        return lookup[(x, y)]
    else:
        # Checking if length of numbers is odd, and making them even
        if (n % 2 == 1):
            y = '0' + y
            x = '0' + x
            n += 1
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
        # Since (a+b)(c+d) = ac + bd + ad + bc, we subtract ac+bd to get ad and bc
        adbc = pq - ac - bd
        return int((10**n) * ac + (10**(half)) * adbc + bd)

def main():
    x = '3141592653589793238462643383279502884197169399375105820974944592'
    y = '2718281828459045235360287471352662497757247093699959574966967627'
    start_time = time.time()
    intk = karatsuba(x, y)
    end_time = time.time()
    print(intk)
    start_time_2 = time.time()
    intxy = int(x) * int(y)
    end_time_2 = time.time()
    print(intxy)
    print(f"{end_time - start_time} vs. {end_time_2 - start_time_2}")

if __name__ == '__main__':
    main()
