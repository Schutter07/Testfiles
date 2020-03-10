from pcinput import getInteger

def main():
    totaal = 0
    for i in range(5):
        totaal += getInteger("Geef een getal: ")
    print("Totaal is", totaal)
    print("Gemiddelde is", totaal/5)

if __name__ == '__main__':
    main()