def main():
    tekst = input("Geef een zin: ")

    klinkers = "aeiou"
    aantal = 0
    for letter in klinkers:
        if letter in tekst:
            aantal += 1

    if aantal == 1:
        print("Er zit 1 verschillende klinker in de string.")
    else:
        print("Er zitten", aantal, "verschillende klinkers in de string.")

if __name__ == '__main__':
    main()