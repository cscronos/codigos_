from dataclasses import dataclass
import proyecto

@dataclass
class Vehiculos:
    costo: int
    capacidad: int
    cargamento: list[list]
    def cant_contenedores(self):
        pass
    
@dataclass
class Barco(Vehiculos):
    def add_array(self, carga):
        self.cargamento.append(carga)
    def cant_contenedores(self):
        print("\nCantidad total de contenedores. =>", len(self.cargamento))

class Tren(Vehiculos):
    def add_array(self, carga):
        self.cargamento.append(carga)
    def cant_contenedores(self):
        print("\nCantidad total de contenedores. =>", len(self.cargamento))

class Avion(Vehiculos):
    def add_array(self, carga): 
        self.cargamento.append(carga)
    def cant_contenedores(self):
        print("\nCantidad total de contenedores. =>", len(self.cargamento))

class Camion(Vehiculos):
    def add_array(self, carga):
        self.cargamento.append(carga)
    def cant_contenedores(self):
        print("\nCantidad total de contenedores. =>", len(self.cargamento))

se_juntaron = []
se_separaron = []
def juntar_todo(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j].tonelaje == 24000:
                se_juntaron.append(x[i][j])
            elif x[i][j].tonelaje == 20000:
                se_juntaron.append(x[i][j])
            elif x[i][j].tonelaje == 22000:
                se_juntaron.append(x[i][j])
            else:
                se_separaron.append(x[i][j])
            
    print("La suma de todos los contenedores y estanques =>",len(se_juntaron))
    print("contenedores y estanques chicos =>",len(se_separaron))
    return se_juntaron

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
        # print('barco muy baratoooooo')
        vip = 40
    elif tren_c < avion_c and tren_c < camion_c:
        # print('tren muy baratoooooo')
        vip = 30
    elif avion_c < camion_c:
        # print('avion muy baratoooooo')
        vip = 20
    elif camion_c < (avion_c / 10) and camion_c < (tren_c / 250) and camion_c < (barco_c / 24000):
        # print('camion muy baratoooooo')
        vip = 10
    else:
        if barco < tren:
            # print('barco rentable')
            cont.append(4)
        if tren < avion:
            # print('tren rentable')
            cont.append(3)
        if avion < camion:
            # print('avion rentable')
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

    # print(barco, tren, avion, camion)
    return barco, tren, avion, camion

array__prueba = []
def organizar_tramporte(a, b, c, d):
    num = 0
    #____ BARCO A 900.000.000
    for i in range(a):
        barcoo = Barco(900000000, 24000, [])
        for j in range(24000):
            barcoo.add_array(se_juntaron[num])
            num += 1
        # AGREGO EL OBJETO BARCO A -
        array__prueba.append(barcoo)
    #____ TREN A 10.000.000
    for i in range(b):
        trenn = Tren(10000000, 250, [])
        for j in range(250):
            trenn.add_array(se_juntaron[num])
            num += 1
        # AGREGO EL OBJETO TREN A -
        array__prueba.append(trenn)
    #____ AVION A 1.000.000
    for i in range(c):
        avionn = Avion(1000000, 10, [])
        for j in range(10):
            avionn.add_array(se_juntaron[num])
            num += 1
        # AGREGO EL OBJETO AVION A -
        array__prueba.append(avionn)
    #____ CAMION A 500.000
    for i in range(d):
        camionn = Camion(500000, 1, [])
        for j in range(1):
            camionn.add_array(se_juntaron[num])
            num += 1
        # AGREGO EL OBJETO AVION A -
        array__prueba.append(camionn)

# CARGAMOS LA VARIABLES
barco, tren, avion, camion = optimizar_vehiculos(len(juntar_todo(proyecto.junta)), camion_c, avion_c, tren_c, barco_c)
organizar_tramporte(barco, tren, avion, camion)

print("\nCantidad total de vehículos => ", len(array__prueba))

print("\nCantidad total de cada tipo de vehículo:")
# print(array__prueba[99].cargamento)
print("Barco :", barco,"/ Tren :", tren,"/ Avion :", avion,"/ Camion :", camion)
print("0 :", barco-1,"   /", barco ,":", barco + tren -1,"   /",barco + tren,":", barco + tren+ avion - 1,"   /",barco + tren+ avion,":",barco + tren+ avion+ camion -1)

# array__prueba[0].cant_contenedores()

# lista_xde = array__prueba[99].cargamento

print()

barco_lista = [] ; tren_lista = [] ; avion_lista = [] ; camion_lista = []

for i in range(0, barco):
    barco_lista.append(i)
for i in range(barco, barco + tren):
    tren_lista.append(i)
for i in range(barco + tren, barco + tren + avion):
    avion_lista.append(i)
for i in range(barco + tren + avion, barco + tren + avion + camion):
    camion_lista.append(i)

# print(barco_lista, tren_lista, avion_lista, camion_lista)
