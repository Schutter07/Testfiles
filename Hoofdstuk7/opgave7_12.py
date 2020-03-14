def main():
    for i in range(1, 101):
        for j in range(1, 10):
            for k in range(j, 10):
                if i == j**2 + k**2:
                    print("{} = {}**2 + {}**2".format(i, j, k))

if __name__ == '__main__':
    main()