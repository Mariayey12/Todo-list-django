🚀 Aplicación de Lista de Tareas
Esta es una aplicación web para gestionar listas de tareas y sus elementos asociados.

🛠️ Tecnologías Utilizadas
Django: Framework web de Python para el desarrollo rápido de aplicaciones.
Python: Lenguaje de programación utilizado para la lógica de backend.
HTML: Lenguaje de marcado para la estructura de la página web.
CSS: Lenguaje de estilo para el diseño visual de la página web.
⚙️ Configuración
Asegúrate de tener Python instalado en tu sistema.
▶️ Cómo Ejecutar la Aplicación
Clona este repositorio en tu máquina local.

Abre una terminal y navega hasta el directorio raíz de la aplicación.

Crea un entorno virtual para el proyecto utilizando virtualenv:

Copy code
python -m venv nombre_del_entorno
Activa el entorno virtual:

En Windows:

Copy code
nombre_del_entorno\Scripts\activate
En macOS y Linux:

bash
Copy code
source nombre_del_entorno/bin/activate
Instala las dependencias del proyecto desde el archivo requirements.txt:

Copy code
pip install -r requirements.txt
Ejecuta el servidor Django con el siguiente comando:

Copy code
python manage.py runserver
Abre un navegador web y accede a http://127.0.0.1:8000/ para ver la aplicación en funcionamiento.

📝 Funcionalidades
Ver todas las listas de tareas: Al acceder a la página principal, se muestran todas las listas de tareas existentes.
Ver elementos de la lista de tareas: Al hacer clic en una lista de tareas, se muestran todos los elementos asociados a esa lista.
Agregar una nueva lista de tareas: Se proporciona un formulario para agregar una nueva lista de tareas.
Agregar un nuevo elemento a la lista de tareas: Se proporciona un formulario para agregar un nuevo elemento a una lista de tareas existente.
Editar elementos de la lista de tareas: Se permite editar los elementos de la lista de tareas existentes.
Eliminar listas de tareas y elementos de la lista: Se proporcionan opciones para eliminar listas de tareas completas o elementos individuales de la lista.
🗃️ Estructura del Código
views.py: Contiene todas las vistas basadas en clases para gestionar la lógica de la aplicación.
models.py: Define los modelos de datos para las listas de tareas y sus elementos asociados.
Plantillas HTML (*.html): Contienen la estructura y el contenido de las páginas web de la aplicación.
🛤️ Rutas
/: Página principal que muestra todas las listas de tareas.
/list/<list_id>: Página que muestra los elementos de una lista de tareas específica.
/list/add/: Página para agregar una nueva lista de tareas.
/list/<list_id>/item/add/: Página para agregar un nuevo elemento a una lista de tareas existente.
/list/<list_id>/item/<item_id>/update/: Página para editar un elemento de la lista de tareas.
/list/<list_id>/item/<item_id>/delete/: Página para eliminar un elemento de la lista de tareas.
📦 Requisitos
asgiref==3.4.1
Django==3.2.9
pytz==2024.1
sqlparse==0.4.4
typing_extensions==4.1.1
¡Y eso es todo! Ahora estás listo para empezar a utilizar esta aplicación para gestionar tus listas de tareas de manera eficiente.

Este README proporciona una visión general de la aplicación, cómo ejecutarla, sus características, estructura de código, rutas disponibles, requisitos de instalación y el uso de un entorno virtual para aislar las dependencias del proyecto
# Proyecto-Tarea-CRUD
Proyecto realizado por parte  parte del autor
👨‍💻 Autor :
Maria Yennifer Martinez Cordero</
T.S.U.en Informatica,
