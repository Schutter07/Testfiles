def main():
    invoer = input()
    lijst = [invoer]
    while invoer != "":
        invoer = input()
        if invoer == "?":
            if lijst != []:
                print(lijst.pop(0))
            else:
                print("FIFO lijst is leeg")
        else:
            lijst.append(invoer)

if __name__ == '__main__':
    main()