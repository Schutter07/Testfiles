def fac(n):
    res = 1
    for i in range(n):
        res *= (i+1)
    return res


def binom(n, k):
    if k < 0 or k > n or n < 0:
        return 0
    return fac(n)/(fac(k)*fac(n-k))


if __name__ == '__main__':
    print(binom(9,4))