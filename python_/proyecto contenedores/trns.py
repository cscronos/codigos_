camion_c = 500000
avion_c = 1000000
tren_c= 10000000
barco_c = 900000000



def optimizar_vehiculos(x, camionC, avionC, trenC, barcoC):
    camion = camionC
    avion = avionC / 10
    tren = trenC / 250
    barco = barcoC / 24000

    cont = [1]
    vip = 0
    if barco_c < tren_c and barco_c < avion_c and barco_c < camion_c:
        print('barco muy baratoooooo')
        vip = 40
    elif tren_c < avion_c and tren_c < camion_c:
        print('tren muy baratoooooo')
        vip = 30
    elif avion_c < camion_c:
        print('avion muy baratoooooo')
        vip = 20
    elif camion_c < (avion_c / 10) and camion_c < (tren_c / 250) and camion_c < (barco_c / 24000):
        print('camion muy baratoooooo')
        vip = 10
    else:
        if barco < tren:
            print('barco rentable')
            cont.append(4)
        if tren < avion:
            print('tren rentable')
            cont.append(3)
        if avion < camion:
            print('avion rentable')
            cont.append(2)

    barco = 0 ; tren = 0 ; avion = 0 ; camion = 0

    while x > 0:
        if vip == 40:
            if x >= 24000:
                barco += 1
                x -= 24000
            else:
                barco += 1
                x = 0
        elif vip == 30:
            if x >= 250:
                tren += 1
                x -= 250
            else:
                tren += 1
                x = 0
        elif vip == 20:
            if x >= 10:
                avion += 1
                x -= 10
            else:
                avion += 1
                x = 0
        elif vip == 10:
            if x >= 1:
                camion += 1
                x -= 1
        else:
            if x >= 24000 and 4 in cont: # BARCO
                barco += 1
                x -= 24000
            elif x >= 250 and 3 in cont: # TREN
                tren += 1
                x -= 250
            elif x >= 10 and 2 in cont: # AVION
                avion += 1
                x -= 10
            else: # CAMION
                camion += 1                                                                                                                             
                x -= 1
    return barco, tren, avion, camion

print(optimizar_vehiculos(234439, camion_c, avion_c, tren_c, barco_c))