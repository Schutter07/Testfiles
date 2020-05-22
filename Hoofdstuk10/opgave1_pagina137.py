def main(woord):
    klinkers = "aeiou"
    teller = 0
    while teller < len(woord):
        if woord[teller] in klinkers:
            print(teller)
        teller += 1


if __name__ == '__main__':
    main("woord")