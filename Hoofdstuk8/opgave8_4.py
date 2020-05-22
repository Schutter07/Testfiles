from math import sqrt


def wortelformule(a, b, c):
    if a == 0:
        if b == 0:
            return 0, 0, 0
        return 1, -c/b, 0
    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return 0, 0, 0
    elif discriminant == 0:
        return 1, -b/(2*a), 0
    else:
        return 2, (-b+sqrt(discriminant))/(2*a), (-b-sqrt(discriminant))/(2*a)


if __name__ == '__main__':
    print(wortelformule(3, 4, -7))
