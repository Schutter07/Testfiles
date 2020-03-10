from pcinput import getInteger

def main():
    x = getInteger("Geef een geheel getal: ")
    if x%2 == 0:
        print("even")
    else:
        print("oneven")

if __name__ == '__main__':
    main()