from pcinput import getInteger

def main():
    teller = 0
    totaal = 0
    while True:
        num = getInteger("Geef een getal: ")
        if num == 0:
            break
        totaal += num
        teller += 1
    print("Totaal is", totaal)
    if teller == 0:
        print("Gemiddelde is", 0)
    else:
        print("Gemiddelde is", totaal / teller)

if __name__ == '__main__':
    main()