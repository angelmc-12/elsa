# Segmentacion de colaboradores ELSA

Este repositorio contiene el flujo de codigo utilizado para generar los segmentos de colaboradores a partir de las encuestas al personal y la organizacion.

# Estructura de carpetas

El proyecto está organizado en las siguientes carpetas:

- **`configs/`** → Contiene archivos con las columnas utilizadas en los algoritmos de segmentación. **No deben modificarse**.
- **`data/`**  
  - `raw/` → Aquí deben colocarse los archivos de encuestas al personal y la organización.  
  - `processed/` → Contiene datos intermedios generados durante el procesamiento. No es necesario modificar esta carpeta.  
- **`outputs/`**  
  - `models/` → Almacena los modelos entrenados que se utilizan para la predicción de segmentos en nuevos datos.  
  - `segments/` → Contiene los resultados de la segmentación que el usuario puede revisar.  
- **`src/`** → Contiene los archivos de código para ejecutar el flujo del proyecto.  
  - **`main.py`** → Archivo principal que orquesta toda la ejecución del proyecto.  
- **`requirements.txt`** → Lista de librerías y versiones necesarias para ejecutar el proyecto.  

Para ejecutar el flujo completo, asegúrate de colocar los archivos de encuestas en `data/raw/` y ejecutar `main.py`.

# Ejecucion de la segmentacion

A continuación, se explican los pasos para descargar el proyecto completo utilizando la terminal.

## Clonar el repositorio

Primero, debes tener git instalado en tu máquina, puedes hacerlo desde la página oficial: https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalaci%C3%B3n-de-Git

También es recomendable instalar Microsoft Visual Studio Build Tools: https://visualstudio.microsoft.com/visual-cpp-build-tools/

Luego, para descargar este proyecto, abre la terminal y ejecuta el siguiente comando:

```sh
git clone https://github.com/angelmc-12/elsa.git
```

## Acceder al directorio del proyecto

Una vez clonado el repositorio, navega dentro de la carpeta del proyecto con:

```sh
cd elsa
```

## Instalación de Dependencias

Antes de ejecutar el proyecto, asegúrate de instalar Python (mínimo versión 3.0) y las librerías necesarias. Para instalar Python, puedes hacerlo desde la página oficial: https://www.python.org/downloads/

Se recomienda utilizar un entorno virtual (venv), puedes activarlo antes de instalar las dependencias. Para ello, abre una terminal y ejecuta los siguiente comandos, para creación y activación:

```sh
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
cd elsa
pip install scipy --prefer-binary
pip install -r requirements.txt 
```

## Ejecucion del proyecto

Para ejecutar el flujo completo, coloca los archivos de encuestas en `data/raw/`, asegurate de que tengan los siguientes nombres:

- **`Encuesta_organizacional_2023.csv`**
- **`Encuesta_personas_2023.csv`**

Y ejecuta:

```sh
python src/main.py
```

# Contacto

Si tienes alguna pregunta o sugerencia, no dudes en crear un issue en el repositorio o contactarme a través de mariomarceloromeroleyva@gmail.com o angelmaytacoaguila@gmail.com.
