def main():
    a = 1
    b = 1
    print(a)
    print(b)
    while True:
        a, b = a+b, a
        if a > 1000:
            break
        print(a)

if __name__ == '__main__':
    main()