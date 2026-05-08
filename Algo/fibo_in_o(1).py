from math import sqrt

# ===============
# using recursion
# ===============
def fibo(n):
    if n <=2:
        return 1

    return fibo(n-1)+fibo(n-2)

# ===============
# using for loop
# ===============
def fibo1(n):
    ls = []
    ls.append(1)
    ls.append(1)
    for i in range(2, n):
        ls.append(ls[i - 1] + ls[i - 2])

    return ls[-1]

# ==========
# D&C
# ==========
mem = {}
def fibo2(n):
    if n <= 2:
        return 1

    if n in mem:
        return mem[n]

    mem[n] = fibo2(n - 1) + fibo2(n - 2)

    return mem[n]


# =================
# get fibo in o(1)
# =================
def fibonacci(n):
    """
    Compute the nth Fibonacci number using Binet's formula.
    """

    sqrt_5 = sqrt(5)

    phi = (1 + sqrt_5) / 2  # Golden ratio
    psi = (1 - sqrt_5) / 2  # Conjugate of the golden ratio

    term1 = (phi**n) / sqrt_5
    term2 = (psi**n) / sqrt_5

    fibonacci_number = term1 - term2

    return int(round(fibonacci_number))


def main():

    n = 40
    print(f"{n} usint o(1): {fibonacci(n):,}")
    print(f"{n} usint fibo: {fibo(n):,}")
    print(f"{n} usint fibo1: {fibo1(n):,}")
    print(f"{n} usint fibo2: {fibo2(n):,}")
    print()

if __name__=='__main__':
    main()
