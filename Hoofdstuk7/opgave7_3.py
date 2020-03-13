from pcinput import getInteger

def main():
    num = getInteger("Geef een getal: ")
    grootste = num
    kleinste = num
    if num % 3 == 0:
        deelbaar = 1
    else:
        deelbaar = 0
    for i in range(9):
        num = getInteger("Geef een getal: ")
        if num > grootste:
            grootste = num
        if num < kleinste:
            kleinste = num
        if num % 3 == 0:
            deelbaar += 1
    print("Grootste is", grootste)
    print("Kleinste is", kleinste)
    print("Aantal deelbaar door 3 is", deelbaar)

if __name__ == '__main__':
    main()