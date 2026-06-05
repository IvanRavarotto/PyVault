import sqlite3
import bcrypt

conexion = sqlite3.connect("pyvault.db")
cursor = conexion.cursor()
cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    first_name TEXT, 
                    last_name TEXT, 
                    birthdate DATE, 
                    email TEXT NOT NULL UNIQUE, 
                    rol TEXT, 
                    password TEXT NOT NULL)""")

def cargar_dato(curso, name, lastN, births, rol, email, password):
    try:
        passwordHash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        print(passwordHash)
        curso.execute("INSERT INTO usuarios (first_name, last_name, birthdate, email, rol, password) VALUES (?, ?, ?, ?, ?, ?)", (name, lastN, births, rol, email, passwordHash))
    except sqlite3.IntegrityError:
        print("Correo ya utilizado/registrado \n¿Desea recuperar la contraseña?")
        
    if (bcrypt.checkpw(password.encode('utf-8'), passwordHash)):
        print("Contraseña correcta")
    else:
        print("Contraseña/Hash erroneo.")

cargar_dato(cursor, "Ivan", "Ravarotto", "2001-19-19", "Ejemplo6@2gmail.com", "Jefe", "Palanca")
conexion.commit()

def buscar(cursor, email):
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", [email])
    emailSearch = cursor.fetchone()
    if (emailSearch != None):
        return emailSearch
    else:
        return None

def mostrar(cursor):
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

#def actualizar()

def borrar(cursor, email):
    cursor.execute("DELETE FROM usuarios WHERE email = ?", [email])
    correo = buscar(cursor, email)
    if correo == None:
        print("Correo borrado con exito")
    
    

print(buscar(cursor, "Ejemplo@gmail.com"))
print(mostrar(cursor))
print(borrar(cursor, "Ejemplo@gmail.com"))
conexion.commit()













