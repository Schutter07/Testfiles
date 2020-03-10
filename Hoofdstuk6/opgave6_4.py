from pcinput import getFloat
from math import sqrt

def main():
    a = getFloat("Geef de waarde van A: ")
    b = getFloat("Geef de waarde van B: ")
    c = getFloat("Geef de waarde van C: ")

    if a == 0:
        if b != 0:
            print("Er is 1 oplossing, namelijk x =", -c/b)
        else:
            print("Er zijn geen oplossingen.")
    else:
        d = b**2 - 4*a*c
        if d < 0:
            print("Er zijn geen oplossingen.")
        elif d == 0:
            print("Er is 1 oplossing, namelijk x =", -b/(2*a))
        else:
            print("Er zijn 2 oplossingen, namelijk x =", (-b+sqrt(d))/(2*a), "en x =", (-b-sqrt(d))/(2*a))


if __name__ == '__main__':
    main()