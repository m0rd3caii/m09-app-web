import mysql.connector
import sys

diccionario = {
    "mercedes": "mcast386@xtec.cat",
    "rayane": "rayane@rayane.sa",
    "mohamed": "moha@gmail.com",
    "jad": "jad@gmail.com",
    "oriol": "joam@gmail.com",
    "elias": "hola123@gmail.com",
    "armau": "arnau@gmail.com",
    "asdrúbal": "asdrubal@gmail.com",
    "adrian": "pedrosanchez@asix2.com",
    "eric": "eric@gmail.com",
    "emma": "pacosanz@gmail.com",
    "nishwan": "nishwan@gmail.com",
    "javi": "javi@gmail.com",
    "novel": "novelferreras49@gmail.com",
    "bruno": "elcigala@gmail.com",
    "david": "argentino@gmail.com",
    "judit": "judit@gmail.com",
    "joao": "joao@gmail.com",
    "laura": "laura@gmail.com",
    "enrico": "123@gmail.com",
    "joel": "joelcobre@gmail.com",
    "aaron": "aaron@gmail.com",
    "moad": "moad@gmail.com"
}

mydb = mysql.connector.connect(
  host="localhost",
  user="rayane",
  password="1234",
  database="data"
)

c = mydb.cursor()

def setup_database(): #Crear tabla si no existe 
  c = mydb.cursor()
  c.execute('''CREATE TABLE IF NOT EXISTS user_info (nombre TEXT, gmail TEXT)''')

conn = setup_database()

def add_data(nombre, gmail): # Añadir datos a la tabla
  c = mydb.cursor()
  c.execute("INSERT INTO user_info (nombre, gmail) VALUES (%s, %s)", (nombre, gmail))
  mydb.commit()

def get_data(nombre): #Consultar datos
    c = mydb.cursor()
    if nombre != "":
        c.execute("SELECT * FROM user_info WHERE nombre = %s", (nombre,))
    else:
        return f"Ohh..."
    result = c.fetchall()
    if result:
        for row in result:
         return f"Nombre: {row[0]}, Correo: {row[1]}"
    else:
        print("Usuario no encontrado")