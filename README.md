markdown
# 🔒 ZeroPass - Herramientas de Seguridad y Productividad

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

Herramienta modular en Python para generación de contraseñas seguras, organización de archivos y web scraping ético.

## 🚀 Características

- 🔑 **Generador de contraseñas seguras** (personalizable)
- 📂 **Organizador automático de archivos** por extensión
- 🌐 **Web scraper ético** (extrae títulos y enlaces)
- 🖥 **Interfaz de menú interactivo**

## 📦 Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/zer0crowd/zeropass.git
   cd zeropass
Instala dependencias:

```bash
pip install -r requirements.txt
🛠 Uso
Ejecuta el menú principal:

```bash
python main.py
Opciones disponibles:
Generar contraseña segura

Longitud personalizable

Incluye mayúsculas, números y símbolos

Organizar archivos

Clasifica automáticamente por tipo (.pdf, .jpg, etc.)

Ejemplo: ./docs/ → ./pdf/documento.pdf

Web scraping (solo para fines educativos)

Extrae título y primeros 5 enlaces de una página

🧩 Estructura del proyecto
text
/zeropass
├── main.py                # Menú principal
├── password_generator.py  # Generador de contraseñas
├── file_organizer.py      # Organizador de archivos
├── web_scraper.py         # Scraper ético
├── requirements.txt       # Dependencias
└── README.md              # Este archivo
⚠️ Limitaciones
El web scraper no funciona en páginas con JavaScript dinámico

Para organizar archivos requiere permisos de escritura

🤝 Contribución
Pull requests son bienvenidos. Para cambios mayores, abre primero un issue.

📜 Licencia
MIT © zer0crowd
