def vriendenlijst():
    invoer = input("Geef de naam van een vriend: ")
    lijst = []
    while invoer != "":
        lijst.append(invoer)
        invoer = input("Geef de naam van een vriend: ")
    lijst.sort()
    for vriend in lijst:
        print(vriend)
    return None

if __name__ == '__main__':
    vriendenlijst()