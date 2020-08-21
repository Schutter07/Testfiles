import opgave10_6

def test1(capsys):
    out = opgave10_6.autocorrect("en zo gebeurde het dat dat onze toevallige ontmoeting \
    met de EErwaarde aRTHUR BElling een ommekeer betekende in ons \
    leven, en vanaf dat moment gingen we iedere zondag naar \
    de kerk van Sint sIMPEL bij Roombroodje MEt Jam.")
    assert out == "En zo gebeurde het dat onze toevallige ontmoeting met de Eerwaarde Arthur Belling een ommekeer betekende in ons leven, en vanaf dat moment gingen we iedere Zondag naar de kerk van Sint Simpel bij Roombroodje Met Jam."


def test2(capsys):
    out = opgave10_6.autocorrect("HET EErste wOORD in deze ZIn is is niet het het enige MET OVerbodige hOOFDLETTERS.")
    assert out == "HET Eerste Woord in deze Zin is niet het enige MET Overbodige Hoofdletters."