from random import randint

kaarten = [(kleur, waarde) for kleur in ["Harten", "Schoppen", "Klaveren", "Ruiten"] for waarde in [2, 3, 4, 5, 6, 7, 8, 9, 10, "Boer", "Dame", "Heer", "Aas"]]
random_kaarten = []
while kaarten != []:
    plaats = randint(0, len(kaarten)-1)
    random_kaarten.append(kaarten[plaats])
    kaarten.pop(plaats)
print(random_kaarten)
