def hanoi(p_van, p_hulp, p_naar, grootte):
    if grootte == 1:
        print("Schijf 1 van {} naar {}".format(p_van, p_naar))
        return 1
    stappen = hanoi(p_van, p_naar, p_hulp, grootte - 1)
    print("Schijf {} van {} naar {}".format(grootte, p_van, p_naar))
    stappen += 1 + hanoi(p_hulp, p_van, p_naar, grootte - 1)
    return stappen


if __name__ == '__main__':
    stappen = hanoi('A', 'B', 'C', 6)
    print(stappen, "stappen gezet!")