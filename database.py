import sqlite3


conexion = sqlite3.connect("pyvault.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, rol TEXT, hash_password TEXT NOT NULL UNIQUE)")

def cargar_usuario(cursor, rol_empleado, hash_password_empleado):
    cursor.execute("INSERT INTO usuarios (rol, hash_password) VALUES (?, ?)", (rol_empleado, hash_password_empleado))
    conexion.commit()
    
def ver_datos(cursor):
    cursor.execute("SELECT * FROM usuarios")
    return cursor.fetchall()

def borrar_dato(cursor, dato):
    
    
    cursor.execute("DELETE FROM usuarios (id) WHERE id = ?", dato)
    cursor.commit()
    
def buscar_dato(cursor, dato):
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (dato))
    
def actualizar_dato(cursor, dato, mod):
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (dato))


print(ver_datos(cursor))
borrar_dato(cursor, 3)
print(ver_datos(cursor))
print(buscar_dato(cursor, 4))
