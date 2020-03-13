def main():
    n = 99

    for i in range(n, 2, -1):
        print("{} flesjes met bier op de muur, {} flesjes met bier.\nOpen er een, drink hem meteen, {} flesjes met bier op de muur.".format(i, i, i-1))
    print("2 flesjes met bier op de muur, 2 flesjes met bier.\nOpen er een, drink hem meteen, 1 flesje met bier op de muur.".format(2, 2, 1))
    print("1 flesje met bier op de muur, 1 flesje met bier.\nOpen er een, drink hem meteen, geen flesjes met bier op de muur.")

if __name__ == '__main__':
    main()