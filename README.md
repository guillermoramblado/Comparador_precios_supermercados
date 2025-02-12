# 🛒 Comparador de Precios de Supermercados

## 📌 Descripción del Proyecto
Este proyecto refleja un **comparador de precios de productos de supermercado**, específicamente de Mercadona, Alcampo y Día, además de ofrecer la posibilidad de **buscar un producto concreto** con las siguientes opciones de filtrado:

- Ordenar productos en orden ascendente/descendente por precio.
- Mostrar productos de uno o varios supermercados específicos.

## 📂 Estructura del Proyecto

- `app/` - Código principal de la aplicación Flask.
- `database/` - Contiene los archivos necesarios para realizar web scraping y obtener los productos de los supermercados.
- `migrations/` - Migraciones de la base de datos, utilizadas para la creación inicial de las tablas `Supermercado` y `Producto`.
- `config.py` - Archivo de configuración de la aplicación.
- `.flaskenv` - Archivo que almacena las variables de entorno utilizadas por Flask.
- `app.db` - Base de datos local ya cargada con los datos de los productos.
- `requirements.txt` - Archivo de texto con los paquetes necesarios a instalar dentro del entorno virtual.

## ⚙️ Instalación y Ejecución

Para ejecutar la aplicación en un entorno local, sigue estos pasos:

### Crear entorno virtual
```sh
python3 -m venv venv
```

### Activar el entorno virtual
```sh
# Windows:
venv\Scripts\activate

# Linux/macOS:
source venv/bin/activate
```

### Instalar dependencias
```sh
pip install -r requirements.txt
```

### Ejecutar la aplicación
```sh
flask run
```

La aplicación estará disponible en la URL que aparece en la terminal. 🌍 

## 🚀 Futuras Mejoras
- **Actualización periódica de productos en la base de datos**  
- **Carrito de compras personalizado para usuarios**  
- **Alertas de variación de precios en productos seleccionados**  

---

## Ejemplos Visuales de la Web

### Home

[![image.png](https://i.postimg.cc/26bvjMb3/image.png)](https://postimg.cc/tZb72rzH)

### Búsqueda de producto

[![image2.png](https://i.postimg.cc/bNQ5NFk6/image.png)](https://postimg.cc/SJxdgdZ8)

### Filtrado de producto

[![image3.png](https://i.postimg.cc/PqNKZ6vn/image.png)](https://postimg.cc/p9bDMJBs)

💡 **¡Espero que este comparador de precios sea de gran utilidad!** 🎯🔥 🚀  

