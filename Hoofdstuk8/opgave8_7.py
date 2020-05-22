# Wat is er fout?
def oppervlakte_van_driehoek(basis, hoogte):
    return 0.5 * basis * hoogte



if __name__ == '__main__':
    basis = 4.5
    hoogte = 1.0
    opp = oppervlakte_van_driehoek(basis, hoogte)
    print("Een driehoek met", basis, "en hoogte",
          hoogte, "heeft oppervlakte", opp)