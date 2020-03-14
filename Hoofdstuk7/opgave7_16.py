from random import random

def main():
    aantal_kruipers = 100000
    aantal_dagen = 0
    for i in range(aantal_kruipers):
        aantal_dagen += 1
        if random() < 2/3:
            aantal_dagen += 1
            while random() < 1/2:
                aantal_dagen += 1
    print(aantal_dagen / aantal_kruipers)

if __name__ == '__main__':
    main()
