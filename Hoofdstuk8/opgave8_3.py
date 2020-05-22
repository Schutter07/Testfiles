def leibniz(num):
    res = 0
    hulp = 1
    for i in range(num):
        res += (-1)**i * (1/hulp)
        hulp += 2
    return 4 * res

if __name__ == '__main__':
    print(leibniz(1))
    print(leibniz(2))
    print(leibniz(3))
    print(leibniz(4))
    print(leibniz(5))
    print(leibniz(50))
