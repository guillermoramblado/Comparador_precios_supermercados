from app import app, db  # Importamos la aplicación y la base de datos
from app.models import Producto, Supermercado
from database.mercadona import categorias_mercadona
from database.dia import categorias_dia
from database.alcampo import categorias_alcampo

def insertar_supermercados():
    """ Inserta los supermercados si no existen en la base de datos. """
    supermercados = [
        {"id": 1, "nombre": "alcampo"},
        {"id": 2, "nombre": "dia"},
        {"id": 3, "nombre": "mercadona"}
    ]
    for supermercado in supermercados:
        db.session.add(Supermercado(id=supermercado["id"], nombre=supermercado["nombre"]))

def insertar_productos(funcion_categorias):
    """ Inserta productos en la base de datos usando una función que retorna la lista de productos a insertar. """
    for nombre, precio, precio_kg, imagen, id_supermercado, nombre_busqueda in funcion_categorias():
        db.session.add(Producto(
            nombre=nombre,
            precio=precio,
            precio_kg=precio_kg,
            url_imagen=imagen,
            id_supermercado=id_supermercado,
            nombre_busqueda=nombre_busqueda
        ))

def insertar_datos():
    with app.app_context():  # Activa el contexto de la aplicación
        insertar_supermercados()  # Inserta los supermercados
        for funcion in [categorias_dia, categorias_alcampo, categorias_mercadona]:
            print("\nInsertando productos de nuevo supermercado...")
            insertar_productos(funcion)  # Inserta productos de cada supermercado

        db.session.commit()  # Confirma las inserciones
        print("Datos insertados correctamente.")

# Ejecutar la inserción solo si el script se ejecuta directamente
if __name__ == "__main__":
    insertar_datos()


