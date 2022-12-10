from dataclasses import dataclass
import MOCK_DATA, leercsv

lista = leercsv.read_csv("MOCK_DATA.csv") # leemos el archivo csv
# lista = MOCK_DATA.read_bd()

@dataclass
class Almacenamiento:
    tipo_carga: str
    masa: str
    tonelaje: int

@dataclass
class Contenedor(Almacenamiento):
    tonelajess: list[int]
    ides: list[str]
    def __post_init__(self):
        if self.tonelaje <= 12000:
            self.tamanho = "pequeño"
        else:
            self.tamanho = "grande"

@dataclass
class Estanques(Almacenamiento):
    tonelajess: int
    ides: str
    def __post_init__(self):
        if self.tonelaje <= 12000:
            self.tamanho = "pequeño"
        else:
            self.tamanho = "grande"

# FILTRO
def filtro_tipo(x, l1, l2, l3, An):
    # x = lista, l1 & l2 & l3 = listas vacias
    #
    # filtro_tipo(lista, mat_nor_sol, mat_nor_liq, mat_nor_gas, xNom_Prod[0])
    cont = 0 ; cont2 = 0 ; cont3 = 0
    for i in range(len(x)):
        #-------------------------
        if x[i][2] == An: # xNom_Prod
            if x[i][3] == "solida":
                cont += int(x[i][4])
                l1.append([int(x[i][4]),int(x[i][0])])

            elif x[i][3] == "liquida":
                cont2 += int(x[i][4])
                l2.append([int(x[i][4]),int(x[i][0])])

            elif x[i][3] == "gas":
                cont3 += int(x[i][4])
                l3.append([int(x[i][4]),int(x[i][0])])
    # print(An,"------")
    # print(cont / 1000,"/",cont2 / 1000,"/", cont3 / 1000)
    # print(cont ,"/",cont2 ,"/", cont3 )
    # print()
    return(l1, l2, l3)
# LISTAS PARA GUARDAR MATERIALES
mat_nor_sol = [] ; mat_nor_liq = [] ; mat_nor_gas = [] # Normal
mat_ref_sol = [] ; mat_ref_liq = [] ; mat_ref_gas = [] # Refrigerada
mat_inf_sol = [] ; mat_inf_liq = [] ; mat_inf_gas = [] # Inflamable

# LISTAS PARA GUARDAR LOS OBJETOS
array_nor_sol = [] ; array_nor_liq = [] ; array_nor_gas = [] # Normal
array_ref_sol = [] ; array_ref_liq = [] ; array_ref_gas = [] # Refrigerada
array_inf_sol = [] ; array_inf_liq = [] ; array_inf_gas = [] # Inflamable

# LISTA NOMBRES PRODUCTOS
xNom_Prod = ["normal","refrigerada","inflamable"]
xNom_Masa = ["solida","liquida","gas"]

# ACTIVAR FILTRO
filtro_tipo(lista, mat_nor_sol, mat_nor_liq, mat_nor_gas, xNom_Prod[0])
filtro_tipo(lista, mat_ref_sol, mat_ref_liq, mat_ref_gas, xNom_Prod[1])
filtro_tipo(lista, mat_inf_sol, mat_inf_liq, mat_inf_gas, xNom_Prod[2])

# AQUÍ JUNTAMOS TODOS LOS CONTENEDORES Y LOS ESTANQUES
junta = [array_nor_sol, array_nor_liq, array_nor_gas,
array_ref_sol, array_ref_liq, array_ref_gas,
array_inf_sol, array_inf_liq, array_inf_gas]

def crear_cont(a, b, c, d, e):
    # a = lista_material ; b = array objetoss ; c = toneladas
    # d = variable productos ; e = variable masa
    #                 a              b          c         d             e
    # crear_cont( mat_nor_sol, array_nor_sol, 24000, xNom_Prod[0], xNom_Masa[0])
    for i in range(len(a)):
        while True:
            if a[i][0] >= c:
                x = Contenedor(d, e, c, c, a[i][1])
                b.append(x)
                a[i][0] = a[i][0] - c
            elif a[i][0] == 0:
                break
            else:
                if i != len(a) - 1:
                    if a[i+1][0] >= c:
                        x = Contenedor(d, e, c, [a[i][0],(c - a[i][0])], [a[i][1], a[i+1][1]])
                        b.append(x)
                        a[i+1][0] = a[i+1][0] - (c - a[i][0])
                        break
                    else:
                        x = Contenedor(d, e, c, [a[i][0],a[i+1][0]], [a[i][1], a[i+1][1]])
                        b.append(x)
                        a[i+1][0] = 0
                        break
                else:
                    if a[i][0] < (c / 2):
                        x = Contenedor(d, e, (c / 2), [a[i][0]], [a[i][1]])
                        b.append(x)
                        break
                    else:
                        x = Contenedor(d, e, (c / 2), (c / 2), [a[i][1]])
                        x2 = Contenedor(d, e, (c / 2), a[i][0] - (c / 2), [a[i][1]])
                        b.append(x)
                        b.append(x2)
                        break

    print("CONTENEDORES -",b[0].tipo_carga,"-", b[0].masa, "-----------",len(b))

def crear_estan(a, b, c, d, e):
    # a = lista.csv ; b = array objetoss ; c = toneladas
    # d = variable productos ; e = variable masa
    for i in range(len(a)):
        while True:  
            if a[i][0] >= c:
                x = Estanques(d, e, c, c, a[i][1])
                b.append(x)
                a[i][0] = a[i][0] - c
            elif a[i][0] == 0:
                break
            else:
                if a[i][0] > (c / 2):
                    x = Estanques(d, e, c, a[i][0], a[i][1])
                    b.append(x)
                    a[i][0] = 0
                    break
                else: 
                    x = Estanques(d, e, (c / 2), a[i][0], a[i][1])
                    b.append(x)
                    a[i][0] = 0
                    break

    print("ESTANQUES -",b[0].tipo_carga,"-", b[0].masa, "-",len(b))


# CONTENEDORES y ESTANQUES
#               A             B          C         D            E
crear_cont(mat_nor_sol, array_nor_sol, 24000, xNom_Prod[0], xNom_Masa[0])
crear_estan(mat_nor_liq, array_nor_liq, 24000, xNom_Prod[0], xNom_Masa[1])
crear_estan(mat_nor_gas, array_nor_gas, 24000, xNom_Prod[0], xNom_Masa[2])

crear_cont(mat_ref_sol, array_ref_sol, 20000, xNom_Prod[1], xNom_Masa[0])
crear_estan(mat_ref_liq, array_ref_liq, 20000, xNom_Prod[1], xNom_Masa[1])
crear_estan(mat_ref_gas, array_ref_gas, 20000, xNom_Prod[1], xNom_Masa[2])

crear_cont(mat_inf_sol, array_inf_sol, 22000, xNom_Prod[2], xNom_Masa[0])
crear_estan(mat_inf_liq, array_inf_liq, 22000, xNom_Prod[2], xNom_Masa[1])
crear_estan(mat_inf_gas, array_inf_gas, 22000, xNom_Prod[2], xNom_Masa[2])