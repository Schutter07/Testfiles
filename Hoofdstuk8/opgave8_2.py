def aantalGemeenschappelijkeLetters(woord1, woord2):
    woord3 = ""
    for letter in woord1:
        if letter in woord2 and letter not in woord3:
            woord3 += letter
    return len(woord3)