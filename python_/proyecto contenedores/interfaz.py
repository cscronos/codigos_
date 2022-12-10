from tkinter import Button, Entry, Frame, Label, Tk, ttk, messagebox, PhotoImage, IntVar
import tkinter
import proyectoP2

room = Tk()
room.title("Containers")
room.resizable(False, False)  # No agrandar la pantalla
room.geometry("800x600")

# VARIABLES
div_width = 800
div_height = 600

bground = ["#33324d"]
frame1 = Frame(room, bg="#1f1e2e").place(x=0, y=0, width=div_width, height=div_height)
frame2 = Frame(frame1, bg=bground[0]).place(x=30, y=30, width=div_width - 60, height=div_height - 100)
def _Home_():
    frame_home = Frame(frame2, bg=bground[0]).place(x=30, y=30, width=div_width - 60, height=div_height - 100)

def _Combobox_(l):
    # LISTAS DE NUMEROS
    list = [proyectoP2.barco_lista, proyectoP2.tren_lista, proyectoP2.avion_lista, proyectoP2.camion_lista]

    combo = ttk.Combobox(
        state="readonly",
        values=list[l]
        )
    list_x = [100, 250, 400, 550]
    combo.current(0)
    combo.place(x=list_x[l], y=220)
    return combo

def _Vehiculos_():
    frame_vehiculos = Frame(frame2, bg=bground[0]).place(x=30, y=30, width=div_width - 60, height=div_height - 100)

    selection = _Combobox_(0)
    selection2 = _Combobox_(1)
    selection3 = _Combobox_(2)
    selection4 = _Combobox_(3)
    
    def show_selection():
        sel = selection.get()
        _tabla_(int(sel))
    def show_selection2():
        sel = selection2.get()
        _tabla_(int(sel))
    def show_selection3():
        sel = selection3.get()
        _tabla_(int(sel))
    def show_selection4():
        sel = selection4.get()
        _tabla_(int(sel))

    Label(frame_vehiculos, text="Vehiculos", font=(
            'Arial', 14), bg=bground[0], fg="#ffffff").place(x=40, y=40)

    # FRAME VEHICULOS
    vehi_x = [100, 250, 400, 550]; nombres_vehiculos = ["Barco", "Tren", "Avion", "Camion"]
    cant_vehi = [proyectoP2.barco, proyectoP2.tren, proyectoP2.avion, proyectoP2.camion ]
    functiones_combox = [show_selection, show_selection2,show_selection3,show_selection4]
    bgFrame_barco = "#1f1e2e"
    for i in range(len(vehi_x)):
        frame_barco = Frame(frame_vehiculos, bg=bgFrame_barco).place(x=vehi_x[i], y=100, width=145, height=100)
        Label(frame_barco, text=nombres_vehiculos[i], font=(
                    'Arial', 14), bg=bgFrame_barco, fg="#ffffff").place(x=vehi_x[i] + 10, y=110)
        Label(frame_barco, text=("Cantidad:", cant_vehi[i]), font=(
                    'Arial', 14), bg=bgFrame_barco, fg="#ffffff").place(x=vehi_x[i] + 10, y=150)
        Button(frame_barco, text=("Ver", nombres_vehiculos[i]), command=functiones_combox[i] , font=('Arial', 10, 'bold'), fg='#7de5c3',
                bg='#197d5c', cursor='hand2', activebackground='#A9CCE3').place(
            x=vehi_x[i], y=190, width=145, height=25)

def _tabla_(num):
    # FRAME
    frame_tabla = Frame(frame2, bg=bground[0]).place(x=30, y=30, width=div_width - 60, height=div_height - 100)

    # TABLA 1
    tabla = ttk.Treeview(columns=('tipo carga', 'masa', 'tamano', 'tonelaje'))
    tabla.place(x=30, y=30, width=div_width - 80, height=div_height - 100)

    tabla.column('#0', width=100, anchor='c')
    tabla.column('#1', width=100, anchor='c')
    tabla.column('#2', width=100, anchor='c')
    tabla.column('#3', width=100, anchor='c')
    tabla.column('#4', width=100, anchor='c')

    # Damos nombre a las cabezas
    tabla.heading('#1', text='TIPO CARGA')
    tabla.heading('#2', text='MASA')
    tabla.heading('#3', text='TAMAÑO')
    tabla.heading('#4', text='TONELAJE')
    tabla.heading('#0', text='ID')

    # SCROLL
    scroll = ttk.Scrollbar(room, orient='vertical', command=tabla.yview)
    scroll.place(x=div_width - 50, y=30, height=div_height - 100, width=20)
    tabla.configure(yscrollcommand=scroll.set)

    # # LEER DATOS
    lista_tabla = proyectoP2.array__prueba[num].cargamento
    # print(lista_tabla)
    lista_tabla.reverse()

    # AGREGAMOS DATOS
    for i in range(0, len(lista_tabla)):
        tabla.insert('', 0, text=lista_tabla[i].ides, values=(lista_tabla[i].tipo_carga, lista_tabla[i].masa, lista_tabla[i].tonelaje, lista_tabla[i].tonelajess, lista_tabla[i].ides))

# BOTONE VER VEHICULOS
cordenadas = [30, 570] ; nombres = ["Vehiculos", "Inicio"]; func_button = [_Vehiculos_, _Home_]
for i in range(len(cordenadas)):
    Button(frame2, text=nombres[i],command=func_button[i] , font=('Arial', 14, 'bold'), fg='#DAD5D6',
            bg='#5499C7', cursor='hand2', activebackground='#A9CCE3').place(
        x=cordenadas[i], y=div_height - 60, width=200, height=30)

# print(proyectoP2.barco)
# proyectoP2.array__prueba[0].cant_contenedores()
room.mainloop()