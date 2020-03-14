def main():
    aantal_piraten = 5
    aantal_kokosnoten = 0
    while True:
        fail = False
        test_aantal = aantal_kokosnoten
        for i in range(aantal_piraten + 1):
            if test_aantal % aantal_piraten == 1:
                test_aantal -= (test_aantal//aantal_piraten) + 1
            else:
                fail = True
                break
        if not fail:
            break
        aantal_kokosnoten += 1
    print(aantal_kokosnoten)

if __name__ == '__main__':
    main()