from pcinput import getInteger

def main():
    num = getInteger("Geef een getal: ")
    for i in range(1, 11):
        print("{} * {} = {}".format(i, num, i*num))

if __name__ == '__main__':
    main()