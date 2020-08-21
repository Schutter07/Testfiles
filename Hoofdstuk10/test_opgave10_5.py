import opgave10_5

def test1(capsys):
    out = opgave10_5.orden_string("ph@t l00t")
    assert out == " 00@hlptt"

def test2(capsys):
    out = opgave10_5.orden_string("Hello, world!")
    assert out == " !,Hdellloorw"

def test3(capsys):
    out = opgave10_5.orden_string("This is not correct???")
    assert out == "   ???Tccehiinoorrsstt"