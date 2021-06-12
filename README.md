# docere
Project final web50

# Descripción

Es un página web echa para los estudiantes y profesores que son profesores y estudiantes.

Es decir, que los profesores pueden inscribirse a clases virtuales, y los estudiantes pueden crear sus propias clases virtuales, teniendo sus respectivas funcionalidades.

# Funcionalidades

- Crear clases públicas y privadas
- Editar/Archivar/Eliminar
- LLevar registros de evaluaciones
- Invitar estudiantes
- Buscar nuevas clases
- Subir archivos para las clases
- Ver perfiles de usuarios
- Agregar información personal
- Supervisar usuarios
- Supervisar clases y evaluaciones

# Tecnologías usadas:
 
- Django
- Bootstrap
- Python, HTML, SCSS, CSS, y un poco de JS.
- Base de datos POSTGRESQ desplegada en Heroku

# Instrucciones para instalarlo y usarlo:

1. Clonar el repositorio.
2. Crear un entorno virtual con pipenv e instalar las dependencias con él *(pipenv shell && pipenv install)*. 
3. Crear un archivo **.env** que contenga lo siguiente:
    DATABASE_URL=<aqui tu base de datos>
    SECRET_KEY=<aqui tu llave secreta>
4. Ejecutar *python manage.py migrate*.
5. Ejecutar *python manage.py runserver*. y listo.

## Elaborado por Axel García, luego de la entrega de este proyecto final, *Docere* será aún trabajado para un uso en Nicaragua.
