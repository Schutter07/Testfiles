def ggd(a, b):
    kleinste = min(a, b)
    grootste = max(a, b)
    rest = grootste % kleinste
    if rest == 0:
        return kleinste
    return ggd(kleinste, rest)


if __name__ == '__main__':
    print(ggd(700, 105))