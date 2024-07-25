# Este proyecto se basa en un modulo de una API REST que esta orientado a el area de la salud especificamente clinica veterinaria donde durante la atencion al paciente se le realiza un estudio y analisis para dar un tratamiento y luego del mismo emitir un tratamiento 🐶

>[!NOTE]
 Aun esta en desarrollo otros modulos 🛠

## Corre el proyecto en local
 1- Clona el repositorio y situate dentro de el
 ``` bash
  git clone https://github.com/leoGlez01/veterinary--manager.git
  ```
  ``` bash
  cd veterinary--manager
  ```
 2- Inicia el entorno
  ``` bash
  python -m venv .venv
  ```
3- Activa el entorno
 ``` bash
  .venv\scripts\activate
  ```
4- Instala las dependencias
 ``` bash
  pip install -r requirements.txt
  ```
5- Crea el archivo .env en el directorio raiz de tu proyecto y establece las variables de entorno
>[!IMPORTANT]
 Toma como ejemplo el archivo .env.example
6- Crea las migraciones
 ``` bash
  py manage.py makemigrations
  ```
7- Migra estas a la base de datos
 ``` bash
  py manage.py migrate
  ```
8- Crea un superusuario para acceder al panel de administracion con este comando y siguiendo las indicaciones de la consola
 ``` bash
  py manage.py createsuperuser
  ```
9- Corre el servidor local
 ``` bash
  py manage.py runserver
  ```
>[!NOTE]
 Puedes entrar al Admin de django en la ruta -> http://localhost:8000/admin/ e iniciar session con las credenciales que antes definistes
