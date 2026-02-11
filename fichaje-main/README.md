# 🕒 Módulo de Fichaje de Asistencia - Odoo 17

Este módulo ha sido desarrollado para gestionar de manera eficiente el registro de jornadas laborales (entradas y salidas) dentro del ecosistema Odoo 17.

## 👤 Autor
* **Mª del Carmen Sánchez Ruiz** 🎓

## 📋 Descripción del Proyecto
El objetivo de esta aplicación es proporcionar una herramienta sencilla para que los empleados registren su asistencia. El sistema garantiza la persistencia de los datos y una interfaz integrada con el resto de módulos de Odoo.

## 🛠️ Tecnologías y Arquitectura
* **ERP**: Odoo 17 (Community Edition). 🖥️
* **Lenguajes**: Python (Lógica de negocio) y XML (Vistas e Interfaz). 🐍
* **Base de Datos**: PostgreSQL 15. 🐘
* **Despliegue**: Docker y Docker Compose para una infraestructura ágil. 🐋
* **Gestión de DB**: pgAdmin 4 para auditoría de tablas. 📊

## 🚀 Instalación y Configuración

### 1. Despliegue de Contenedores
Asegúrate de tener instalado Docker y ejecuta desde la terminal:
```bash
docker-compose up -d
Instalación del Módulo
Para cargar los archivos en el servidor Odoo:

Copia los archivos al volumen de addons:

Bash
docker cp . odoo:/mnt/extra-addons/fichaje
Reinicia el contenedor para que Odoo detecte los cambios:

Bash
docker restart odoo
En Odoo, accede a Aplicaciones, quita el filtro predeterminado y busca "Fichaje de Asistencia" para instalarlo.

🔒 Seguridad y Acceso
Se ha implementado el archivo ir.model.access.csv para definir los permisos de lectura, creación y escritura del modelo fichaje.asistencia, permitiendo que el menú sea visible para los usuarios autorizados. 🔑

📂 Estructura del Módulo
models/: Definición de la lógica y campos (employee_id, fecha_fichaje, tipo_accion).

views/: Diseño de las interfaces de usuario (vistas de tipo list y form).

security/: Reglas de acceso al sistema.

__manifest__.py: Metadatos e inventario del módulo.



