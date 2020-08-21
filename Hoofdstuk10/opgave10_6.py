def autocorrect(tekst):
    if len(tekst) <= 0:
        return tekst
    output = tekst[0].upper() + tekst[1:]
    woordlijst = output.split()
    output = ""
    laatstewoord = ""

    for woord in woordlijst:
        # Duplicaten verwijderen
        if woord == laatstewoord:
            continue

        # Dubbele hoofdletters correctie
        if len(woord) > 2 and woord[0] >= 'A' and woord[0] <= 'Z' and \
            woord[1] >= 'A' and woord[1] <= 'Z' and \
            woord[2] >= 'a' and woord[2] <= 'z':
            woord = woord[0] + woord[1].lower() + woord[2:]

        # Dagen met hoofdletter
        dag  = woord.lower()
        if dag in ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"):
            print(dag)
            woord = dag[0].upper() + dag[1:]

        # CAPS LOCK correctie
        if woord[0].lower() == woord[0] and woord[1:].upper() == woord[1:]:
            woord = woord[0].upper() + woord[1:].lower()

        output += woord + " "
        laatstewoord = woord

    output = output.strip()
    return output

if __name__ == '__main__':
    zin = "en zo gebeurde het dat dat onze toevallige ontmoeting \
    met de EErwaarde aRTHUR BElling een ommekeer betekende in ons \
    leven, en vanaf dat moment gingen we iedere zondag naar \
    de kerk van Sint sIMPEL bij Roombroodje MEt Jam."
    print(autocorrect(zin))