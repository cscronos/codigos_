import mysql.connector
import leercsv

lista = leercsv.read_csv("MOCK_DATA.csv")

conn = mysql.connector.connect(
    host="db.inf.uct.cl",
    user="A2020_jdelpino",
    password="A2020_jdelpino",
    database="A2020_jdelpino"
)

mycursor = conn.cursor()

ingresar = "INSERT INTO `Productos`(`id`,`nombre_producto`,`tipo`,`masa`,`peso`) VALUES"

for i in range(len(lista)):
    ingresar += f" ({lista[i][0]},'{lista[i][1]}','{lista[i][2]}','{lista[i][3]}',{lista[i][4]}),"

ingresar2_0 = ingresar[:-1] + ";"

try:
   mycursor.execute(ingresar2_0)
   conn.commit()
except:
   conn.rollback()

conn.close()
