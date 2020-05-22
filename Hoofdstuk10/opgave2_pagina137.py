def main(woord1, woord2):
    teller = 0
    while teller < len(woord1) and teller < len(woord2):
        if woord1[teller] == woord2[teller]:
            print(teller)
        teller += 1


if __name__ == '__main__':
    main("The Holy Grail", "Life of Brian")