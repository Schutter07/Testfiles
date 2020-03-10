from math import sqrt
from pcinput import getFloat

def main():
    a = getFloat("Geef de lengte van de eerste rechthoekzijde: ")
    b = getFloat("Geef de lengte van de tweede rechthoekzijde: ")
    print("Een rechthoekige driehoek met als rechthoekzijden", a, "en", b, "heeft als schuine zijde",
          sqrt(a ** 2 + b ** 2))


if __name__ == '__main__':
    main()
