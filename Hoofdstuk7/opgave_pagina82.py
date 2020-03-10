def main():
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j:
                print("({},{})".format(i, j))

if __name__ == '__main__':
    main()