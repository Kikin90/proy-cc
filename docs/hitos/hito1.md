# Hito #1

LibroWave Version 1.1

## Contenido de este Hito

- [Hito #1](#hito-1)
  - [Contenido de este Hito](#contenido-de-este-hito)
  - [Historias de Usuarios](#historias-de-usuarios)
  - [Milestones](#milestones)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Lenguaje de desarrollo y Framework](#lenguaje-de-desarrollo-y-framework)

<a name="us"></a>

## Historias de Usuarios

**US-1:** [Como Bibliotecario, poder gestionar los usuarios clientes de la Biblioteca.](https://github.com/Kikin90/proy-cc/issues/1)

**US-2:** [Como bibliotecario, poder gestionar los libros de la Biblioteca.](https://github.com/Kikin90/proy-cc/issues/2)

**US-3:** [Pedir préstamo de uno o varios Libros.](https://github.com/Kikin90/proy-cc/issues/3)

**US-4:** [Búsqueda de un Libro, por su título o por Autor.](https://github.com/Kikin90/proy-cc/issues/4)

**US-5:** [Realizar comentario sobre un libro leído.](https://github.com/Kikin90/proy-cc/issues/5)


<a name="ms"></a>

## Milestones

**MS-1:** [Definición y creación del proyecto.](https://github.com/Kikin90/proy-cc/milestone/1)

**MS-2:** [Definición y creación de pruebas unitarias.](https://github.com/Kikin90/proy-cc/milestone/2)

**MS-3:** [Creación de contenedores.](https://github.com/Kikin90/proy-cc/milestone/3)

**MS-4:** [Desarrollo del servicio.](https://github.com/Kikin90/proy-cc/milestone/4)

**MS-5:** [Integración continua del proyecto.](https://github.com/Kikin90/proy-cc/milestone/5)

**MS-6:** [Despliegue del servicio con contenedores.](https://github.com/Kikin90/proy-cc/milestone/6)

<a name="ps"></a>

## Estructura del Proyecto

El proyecto esta  estructurado por los libros de la biblioteca, los usuarios y los préstamos que tiene cada libro.
Se tienen 4 clases principales, que son guardadas en tablas de la base de Datos.
Libro
Usuario
Préstamo
Comentario

Por ejemplo el modelo de la clase Libro es el siguiente:

```
class Book(Document):
    title= StringField(required=True)
    author= StringField()
    genre= StringField()
    description= StringField()
    isbn= StringField(unique=True)
    image= StringField()
    published= DateTimeField()
    publisher= StringField()
```

<a name="ldf"></a>

## Lenguaje de desarrollo y Framework

Como lenguaje de desarrollo se utilizara Python y el framework de python Django.
Usaremos docker-compose como entorno de desarrollo. Esto nos proporciona independencia con respecto al portatil, facilidad de instalación de librerías, BDs. etc, uniformidad entre todos, facilidad de despliegue, etc.

Para el diseño de la página en el front-end usaremos algún CSS Framework que nos facilite la actividad y el framework más popular es Bootstrap. 
