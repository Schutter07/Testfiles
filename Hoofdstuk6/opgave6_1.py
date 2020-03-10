from pcinput import getFloat

def main():
    cijfer = getFloat("Geef het cijfer: ")
    if cijfer > 10:
        print("Foutmelding")
    elif cijfer >= 8.5:
        print("A")
    elif cijfer >= 7.5:
        print("B")
    elif cijfer >= 6.5:
        print("C")
    elif cijfer >= 5.5:
        print("D")
    elif cijfer >= 0:
        print("F")
    else:
        print("Foutmelding")


if __name__ == '__main__':
    main()