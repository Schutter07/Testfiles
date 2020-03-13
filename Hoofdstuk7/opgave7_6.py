def main():
    woord1 = input("Geef het eerste woord: ")
    woord2 = input("Geef het tweede woord: ")
    woord3 = ""

    for letter in woord1:
        if letter in woord2:
            if letter not in woord3:
                woord3 += letter
    print("De gemeenschappelijke letters zijn:", woord3)

if __name__ == '__main__':
    main()