def alleen_letters(zin):
    output = ""
    for letter in zin:
        if (letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z'):
            output += letter
        else:
            output += " "
    return output


if __name__ == '__main__':
    print(alleen_letters("ph@t l00t"))