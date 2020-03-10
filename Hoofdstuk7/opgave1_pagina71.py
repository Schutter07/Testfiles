from pcinput import getInteger

def main():
    totaal = 0
    teller = 0
    while teller < 5:
        totaal += getInteger("Geef een nummer: ")
        teller += 1
    print("Totaal is", totaal)
    print("Gemiddelde is", totaal / teller)

if __name__ == "__main__":
    main()