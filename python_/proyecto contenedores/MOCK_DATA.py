import mysql.connector

conn = mysql.connector.connect(
    host="db.inf.uct.cl",
    user="A2020_jdelpino",
    password="A2020_jdelpino",
    database="A2020_jdelpino"
)

mycursor = conn.cursor()
mycursor.execute("SELECT * FROM Productos")

myresult = mycursor.fetchall()
conn.close()

def read_bd():
    lista = []
    for x in myresult:
        lista.append([x[0],x[1],x[2],x[3],x[4]])
    return lista