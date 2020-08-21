def orden_string(tekst):
    antw = ""
    while tekst != "":
        kleinste = tekst[0]
        teller = 1
        plaats = 0
        while teller < len(tekst):
            if kleinste > tekst[teller]:
                kleinste = tekst[teller]
                plaats = teller
            teller += 1
        antw += kleinste
        tekst = tekst[:plaats] + tekst[plaats+1:]
    return antw

if __name__ == '__main__':
    print(orden_string("Hello, world!"))
    print(orden_string("ph@t l00t"))
    print(orden_string("This is not correct???"))
