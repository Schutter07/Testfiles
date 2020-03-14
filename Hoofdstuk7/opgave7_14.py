def main():
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                for l in range(1, 10):
                    if (i*1000 + j*100 + k*10 + l) == 4*(l*1000 + k*100 + j*10 + i):
                        print("A =", l)
                        print("B =", k)
                        print("C =", j)
                        print("D =", i)

if __name__ == '__main__':
    main()