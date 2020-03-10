from pcinput import getFloat

def main():
    num1 = getFloat("Geef het eerste getal: ")
    num2 = getFloat("Geef het tweede getal: ")
    num3 = getFloat("Geef het derde getal: ")

    grootste = max(num1, num2, num3)
    kleinste = min(num1, num2, num3)
    gemiddelde = round((num1 + num2 + num3)/3, 2)
    print("Grootste:", grootste)
    print("Kleinste:", kleinste)
    print("Gemiddelde:", gemiddelde)
if __name__ == '__main__':
    main()