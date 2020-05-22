import opgave8_2

def test1(capsys):
    out = opgave8_2.aantalGemeenschappelijkeLetters("een", "peer")
    assert out == 1

def test2(capsys):
    out = opgave8_2.aantalGemeenschappelijkeLetters("Zevende", "zwevende")
    assert out == 4

def test3(capsys):
    out = opgave8_2.aantalGemeenschappelijkeLetters("Appelsap", "poivre")
    assert out == 2
