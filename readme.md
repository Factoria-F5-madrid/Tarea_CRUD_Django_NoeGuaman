
# Tarea: Investigación y Desarrollo de un CRUD con Django

## Parte 1: Aplicación CRUD y Django

### 1. ¿Qué es un CRUD y cuál es su propósito en el desarrollo de aplicaciones web? Añade un ejemplo de aplicación web que use una estructura de CRUD 

Un CRUD es el conjunto de operaciones básicas que permiten crear, consultar, modificar y eliminar datos en una base de datos desde una aplicación web. Es la base para que el frontend y el backend se comuniquen correctamente. A estas operaciones se les puede añadir lógica adicional, como validaciones, control de acceso o seguridad en las comunicaciones para proteger los datos del usuario.


Ejemplos de aplicaciones:
- Redes sociales (facebook, BlueSky, Instagram…)
- Tableros kanban (Trello, Jira, Odoo…)

### 2. ¿Qué son los patrones de arquitectura en desarrollo de software? 

Son esquemas de organización que indican cómo dividir una aplicación en componentes y cómo se comunican entre sí.
Su objetivo es:
- Separar responsabilidades (p. ej., lógica de negocio vs. interfaz de usuario).
- Facilitar mantenimiento y pruebas (cambias una parte sin romper el resto).
- Favorecer escalabilidad y reutilización (el mismo patrón se aplica en diferentes proyectos).

Piensa en ellos como el plano de un edificio: no dictan el color de las paredes, pero sí dónde van habitaciones, tuberías y cables.

### ¿Qué es el patrón MVC (Modelo–Vista–Controlador)?

| Componente | Responsabilidad (muy resumida) | 
|---|---|
|Modelo | Gestiona datos y reglas de negocio. Sabe leer / escribir en la BD.|
|Vista | Presenta los datos al usuario (HTML, JSON, GUI…).|
|Controlador | Interpreta las peticiones, pide datos al Modelo y decide qué Vista mostrar. |

Flujo típico:
1. Usuario hace una petición (clic, URL, botón).
2. El Controlador la interpreta.
3. Llama al Modelo para obtener / guardar datos.
4. Pasa esos datos a la Vista, que genera la respuesta (página, API, etc.).

### ¿Qué es el patrón MVT (Modelo–Vista–Template)?

Es la variante que popularizó Django. Cambia sobre todo el nombre de las piezas:

| Componente Django | Equivalencia en MVC | Responsabilidad en Django                                                                 |
|-------------------|---------------------|--------------------------------------------------------------------------------------------|
| Modelo            | Modelo              | Igual: lógica y acceso a datos mediante el ORM.                                           |
| Vista             | Controlador         | Función o clase que recibe la petición HTTP, consulta modelos y devuelve una respuesta.   |
| Template          | Vista               | Archivo de plantilla (HTML + etiquetas) que renderiza la presentación final.              |

Django _“esconde”_ parte del controlador en su motor de mapeo de URLs y en las clases View; por eso llama Vista a lo que en MVC sería el Controlador.

### Diferencias clave entre MVC y MVT

| Aspecto                        | MVC                                 | MVT (Django)                                                                 |
|-------------------------------|--------------------------------------|------------------------------------------------------------------------------|
| Nombre de piezas              | Modelo, Vista, Controlador           | Modelo, Vista, Template                                                     |
| Dónde va la lógica de negocio | Modelo                               | Modelo                                                                      |
| Quién procesa la petición     | Controlador                          | Vista (función / clase)                                                     |
| Quién genera la salida final  | Vista (HTML, etc.)                   | Template + motor de plantillas                                              |
| Quién maneja el enrutado      | Normalmente el Controlador           | Django (`urls.py`) + Vista                                                  |
| Sensación para el desarrollador | Escribes Controlador y Vista explícitamente | En muchos casos solo escribes Vistas y Templates; el framework hace de “mini-controlador” automático |

En resumen: la separación de responsabilidades es la misma, pero Django rebautiza las cajas y automatiza parte del flujo.
### ¿Cuál de estos dos patrones se usa en Django?
Django usa MVT.
En tu código definirás Modelos en models.py, Vistas (funciones o clases) en views.py y Templates (HTML) en la carpeta templates/.
El framework se encarga del enrutado HTTP y de enlazar todo con su ORM y su sistema de plantillas.

Idea para recordar
MVC = Controlador + Vista
MVT = Vista (Django) + Template

### 3. ¿Cómo se estructura un proyecto en Django? Explicar brevemente el rol de los modelos, vistas, templates y URLs.

Estructura básica de un proyecto Django
```
mi_proyecto/
├── mi_proyecto/        # Configuración global
├── mi_app/             # App individual (modelos, vistas, templates, etc.)
|      ├── models.py
|      ├── views.py
|      ├── templates.py
|      ├── urls.py
├── manage.py
```
Django usa una arquitectura propia que se llama MTV, Modelo Vista Template que se basa en la MVC pero con sus propias peculiaridades.

Para entenderlo vamos a tener en cuenta el Modelo Vista Controlador (MVC)

El **modelo** en Django sigue siendo **modelo** (modelo.py):

- Controla el comportamiento de los datos.
- Define los datos almacenados
- Se encuentra en forma de clases de Python(el modelo es un objeto).
- Cada tipo de dato que debe ser almacenado se encuentra en una variable con ciertos parámetros.
- Posee métodos para la gestión de los datos.

La **vista** en Django se llama **plantilla/template** (views.py) :

- Se presenta en forma de funciones o clases en Python,
- su propósito es determinar qué datos serán visualizados.

	“El ORM de Django permite escribir código Python en lugar de SQL para hacer las consultas que necesita la vista”
- La vista también se encarga de tareas conocidas como el envío de correo electrónico, la autenticación con servicios externos y la validación de datos a través de formularios.	
- La vista no tiene nada que ver con el estilo de presentación de los datos, sólo se encarga de los datos, la presentación es tarea de la plantilla.

El **controlador** en Django se llama **vista** (templates.py):

- Es básicamente una página HTML con algunas etiquetas extras propias de Django, no solamente crea contenido en HTML (también XML, CSS, Javascript, CSV, etc).
- La plantilla (Template) recibe los datos de la vista y luego los organiza para la presentación al navegador web

Respecto a las **URLs** Django posee el control sobre la configuración de las rutas. Posee un mapeo de URLs que permite controlar el despliegue de las vistas apropiadas para la solicitud y pasar cualquier variable que la vista necesite para completar su trabajo, además permite que las rutas que maneje Django sean agradables y entendibles para el usuario.


###  ¿Para qué se usa el signo “%%” en los templates?

En los templates de Django, las etiquetas con {% %} se utilizan para ejecutar lógica, como bucles, condiciones, o cargar plantillas. Las variables con {{ }} se usan para mostrar el contenido de variables o expresiones en el HTML generado.

Ejemplos:
```
{% if %} → ejecuta condicionales

{{ nombre_usuario }} → mostraría el valor de la variable nombre_usuario en la plantilla
```
### 4. ¿Cuál es el flujo de datos entre un formulario HTML y la base de datos en Django?

![Flujo de datos](https://github.com/Factoria-F5-madrid/Tarea_CRUD_Django_NoeGuaman/blob/main/assets/flujo-datos.png?raw=true)

Cuando un usuario llena un formulario en una página web y hace clic en "Enviar", los datos se envían al servidor, donde Django los recibe. Esos datos llegan a una función llamada "vista",las vistas son funciones o clases en Django que se encargan de recibir una petición (como un formulario enviado) y devolver una respuesta. Luego, con esos datos, Django crea un nuevo objeto usando un modelo (que es como una plantilla de cómo deben guardarse los datos). Finalmente, ese objeto se guarda en la base de datos. 
Después de guardar, Django puede mostrarle al usuario una página de confirmación o llevarlo a otra parte del sitio.

### 5.  ¿Qué herramientas o comandos ofrece Django para facilitar el desarrollo de un CRUD, para qué es cada una? (Por ejemplo: startapp, makemigrations, migrate, runserver, ModelForm, admin, etc.) 
Como ocurre en la mayoría de frameworks, Django incluye herramientas, automatizaciones y comandos que facilitan el desarrollo, especialmente de estructuras CRUD.

Comandos que se ejecutan en todos los proyectos:
- startproject: Sirve para crear la estructura básica de un nuevo proyecto en Django. Esto incluye la creación de una carpeta con el nombre del proyecto y dentro de ella, archivos de configuración y un módulo de administración. No crea una aplicación web en sí misma, sino un esqueleto sobre el cual construir. 
- startapp: Sobre el esqueleto anterior, crea la estructura básica de una aplicación en Django. Aquí es donde se construyen los modelos, vistas, formularios y URLs necesarios para el CRUD.
- makemigrations: Detecta los cambios en los modelos (por ejemplo, agregar un nuevo campo al modelo) y genera archivos de migración que describen cómo debe cambiar la base de datos.
- migrate: Aplica las migraciones a la base de datos real, creando o modificando tablas para que coincidan con los modelos.
- runserver: Inicia un servidor de desarrollo local para probar la aplicación en tiempo real mientras se desarrolla.
- shell (python manage.py shell): Abre una consola interactiva para probar modelos, consultar datos y hacer operaciones CRUD directamente desde Python. Por ejemplo para probar una operación GET sin tener que escribir el HTML.

Vistas genéricas (Class-Based Views): Django incluye vistas como ListView, CreateView, UpdateView, y DeleteView que permiten implementar los archivos que necesita para el CRUD rápidamente.
- ListView: Muestra una lista de objetos.
- DetailView: Muestra los detalles de un objeto específico.
- CreateView: Permite la creación de un nuevo objeto.
- UpdateView: Permite la actualización de un objeto existente.
- DeleteView: Permite la eliminación de un objeto.
  
Como se puede ver la mayoría de los comandos que más se usan están orientados a administrar la base de datos y los archivos que necesita para el CRUD, que es de las mayores peculiaridades de Django.
Algo muy importante de porque es un framework y tiene herramientas de tal:
- Model: Define la estructura de la base de datos. Cada modelo representa una tabla y cada atributo una columna. Es lo más básico para crear el CRUD, ya que de ahí se genera toda la lógica de definición del tipo de datos y nombres para el JSON, por lo tanto hay que tenerla muy en cuenta para interactuar con las tablas.
- ModelForm: Permite generar formularios automáticamente a partir de un modelo. Facilita las operaciones de crear y actualizar datos con validación y envío integrados.
- admin: Django genera una interfaz de administración automática a partir de los modelos. Es una forma rápida de gestionar datos con operaciones CRUD sin tener que programar nada de frontend. También permite a los futuros propietarios de la aplicación tener bastante autogestión, incluso sin ninguna formación.
- createsuperuser: Crea un usuario administrador para acceder al panel de administración (nombrado arriba) y gestionar los modelos registrados, entre otras cosas.
  
Estas herramientas ayudan a automatizar muchas tareas repetitivas, mantener el código organizado y desarrollar aplicaciones web robustas de forma más rápida.


### 6. ¿Cómo funciona el Admin de Django?  

El panel de administración de Django es una herramienta de interfaz web generada automáticamente a partir de los modelos definidos en el proyecto.
Su objetivo es facilitar el trabajo de administradores y editores, permitiendo gestionar la base de datos sin necesidad de escribir código.

¿Cómo funciona?
1. Uso de modelos como base
   
- Django toma las clases definidas en el archivo models.py como base para crear el panel de administración.
- Cada clase representa una tabla de la base de datos y define los campos que se van a administrar.

2. Registro en el panel
Para que un modelo aparezca en el panel de administración, debe registrarse en el archivo admin.py.

Ejemplo:
```
from django.contrib import admin
from .models import MiModelo
admin.site.register(MiModelo)
```

3. Autenticación y permisos
Django incluye un sistema de autenticación que permite controlar el acceso al panel.

Algunas funcionalidades clave:
- Solo los usuarios staff pueden ingresar al panel.
- Se puede crear un superusuario con todos los permisos.
- Es posible asignar permisos personalizados a cada usuario.

4. Interfaz automática y personalizable
   
La interfaz generada permite:
-  Agregar, editar, eliminar y ver registros de cualquier modelo.
- Buscar, filtrar y ordenar datos fácilmente.
- Personalizar formularios, listas y secciones del panel mediante configuraciones en admin.py.

