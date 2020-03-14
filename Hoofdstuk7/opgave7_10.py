from math import sqrt
from pcinput import getInteger

def main():
    num = getInteger("Geef een getal: ")
    if num <= 1:
        print("Het getal is niet priem!")
    elif num == 2:
        print("Het getal is priem!")
    else:
        for i in range(2, int(sqrt(num))):
            if num % i == 0:
                print("Het getal is niet priem!")
                break
        else:
            print("Het getal is priem!")

if __name__ == '__main__':
    main()