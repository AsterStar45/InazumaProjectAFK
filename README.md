# InazumaAFK

Bot automático basado en **OCR (reconocimiento de texto en pantalla)** para automatizar acciones repetitivas dentro del juego.  
El bot detecta textos en regiones específicas de la pantalla y responde con clics o teclas según reglas configurables.

La aplicación cuenta con:
- Motor OCR usando Tesseract
- Automatización con PyAutoGUI
- Interfaz gráfica en PySide6
- Soporte para distintas resoluciones

---

## Requisitos

### 1. Python
Versión recomendada: **Python 3.10 o superior**

Verifica tu versión:
```bash
python --version
```

---

### 2. Tesseract OCR (OBLIGATORIO)

El bot **NO funciona sin Tesseract instalado**.

#### Descargar Tesseract (Windows)
Repositorio oficial:  
https://github.com/UB-Mannheim/tesseract/wiki

Instala la versión para Windows (64 bits).

Durante la instalación:
- Marca la opción **Add Tesseract to PATH**
- Idioma recomendado: English

Ruta por defecto usada en el proyecto:
```txt
C:\Program Files\Tesseract-OCR\tesseract.exe
```

Si instalas en otra ruta, debes modificarla en el código.

---

### 3. Dependencias del proyecto

Instala las dependencias con:
```bash
pip install -r requirements.txt
```

---

## Uso del bot (MUY IMPORTANTE)

### Ejecutar como administrador
Para que el bot pueda:
- Leer correctamente la pantalla
- Enviar teclas
- Hacer clics sobre el juego

**Debes ejecutar el programa como administrador**, tanto el `.exe` como el `.py` si vas a modificar el código.

---

### Configuración del Equipo Rival

En la interfaz gráfica existe un campo llamado **Equipo rival**.

Debes escribir el nombre del equipo rival usando:
- Letras en MAYÚSCULA
- Separadas por comas
- Usando solo las primeras 2 o 3 letras de cada palabra

#### Ejemplo

Equipo:
```
Luz Eterna
```

Opciones válidas:
```
LUZ,ETE
LU,ET
```

Recomendación:
- Empieza con 3 letras
- Si el OCR falla, prueba con 2

Esto se usa para detectar el texto del equipo rival en pantalla mediante OCR.

---

### Pasos para usar el bot correctamente

1. Ejecuta el programa **como administrador**
2. Escribe el **Equipo rival** en el campo correspondiente
3. Abre el juego
4. Entra al partido del equipo rival correspondiente
5. Presiona **Iniciar bot**
7. Deja el juego en **primer plano** (no minimizado)
8. No muevas la ventana del juego mientras el bot esté activo

Si todo está bien configurado, el bot funcionará automáticamente.

---

## Resolución de pantalla

Las regiones del bot están definidas en **porcentajes**, no en píxeles fijos.

Esto permite que el bot funcione en todas las resoluciones, como por ejemplo:
- 1920x1080
- 1366x768
- 2560x1440

Aun así:
- El juego debe estar en pantalla completa o modo ventana sin bordes
- No se recomienda cambiar la resolución mientras el bot esté activo

---

## Crear el ejecutable

El proyecto puede compilarse en un solo `.exe` usando PyInstaller.

Comando recomendado (PowerShell en una sola línea):
```powershell
pyinstaller --onefile --windowed --name InazumaAFK --icon assets/icon.ico --add-data "assets/icon.ico;assets" main.py
```

El ejecutable final se generará en:
```
dist/InazumaAFK.exe
```

---

## Notas importantes

- El OCR no es perfecto, por eso se usan coincidencias parciales
- Si una región falla, ajusta las palabras clave
- No ejecutes el bot en segundo plano
- No minimices el juego
- Solo hay soporte para idioma del juego en Español

---
