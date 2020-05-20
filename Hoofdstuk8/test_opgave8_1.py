import opgave8_1

def test1(capsys):
    opgave8_1.tafels(7)
    out, err = capsys.readouterr()
    assert out == '1 * 7 = 7\n2 * 7 = 14\n3 * 7 = 21\n4 * 7 = 28\n5 * 7 = 35\n6 * 7 = 42\n7 * 7 = 49\n8 * 7 = 56\n9 * 7 = 63\n10 * 7 = 70\n'
    assert err == ''

def test2(capsys):
    opgave8_1.tafels(12)
    out, err = capsys.readouterr()
    assert out == '1 * 12 = 12\n2 * 12 = 24\n3 * 12 = 36\n4 * 12 = 48\n5 * 12 = 60\n6 * 12 = 72\n7 * 12 = 84\n8 * 12 = 96\n9 * 12 = 108\n10 * 12 = 120\n'
    assert err == ''

def test3(capsys):
    opgave8_1.tafels(-5)
    out, err = capsys.readouterr()
    assert out == '1 * -5 = -5\n2 * -5 = -10\n3 * -5 = -15\n4 * -5 = -20\n5 * -5 = -25\n6 * -5 = -30\n7 * -5 = -35\n8 * -5 = -40\n9 * -5 = -45\n10 * -5 = -50\n'
    assert err == ''