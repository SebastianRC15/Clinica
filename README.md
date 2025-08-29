# Sistema de Gestión de Clínicas

Este proyecto es un sistema de gestión para clínicas médicas desarrollado con Django. Permite administrar clínicas, pacientes, citas médicas y ubicaciones geográficas (ubigeo).

#Participantes:

-Cesar Martel SC
-Miguel Ruiz
-Sebastian Rosas

## Estructura del Proyecto

El proyecto está organizado en las siguientes aplicaciones:

- **Config**: Configuración principal del proyecto Django
- **clinica**: Gestión de clínicas
- **paciente**: Gestión de pacientes
- **cita**: Gestión de citas médicas
- **ubigeo**: Gestión de ubicaciones geográficas (departamentos, provincias, distritos)

## Modelos de Datos

### Clínica
- Nombre
- Dirección
- Teléfono
- Email
- Estado (activo/inactivo)
- Fecha de creación

### Paciente
- Clínica a la que pertenece
- Nombres
- Apellidos
- DNI (único)
- Fecha de nacimiento
- Teléfono
- Email (opcional)
- Dirección
- Ubigeo (ubicación geográfica)
- Estado (activo/inactivo)
- Fecha de registro

### Cita
- Clínica
- Paciente
- Fecha y hora
- Motivo
- Observaciones (opcional)
- Estado (programada, confirmada, atendida, cancelada)
- Ubicación de la cita (ubigeo)
- Fecha de creación

### Ubigeo
- Clínica
- Departamento
- Provincia
- Distrito
- Código postal (opcional)
- Estado (activo/inactivo)
- Fecha de creación

## Requisitos

- Python 3.x
- Django 5.2.5
- MySQL
- PyMySQL 1.1.0

## Instalación

1. Clona este repositorio:
   ```
   git clone <url-del-repositorio>
   cd UBIGEO-MULTI-NEW
   ```

2. Crea un entorno virtual e instala las dependencias:
   ```
   python -m venv venv
   venv\Scripts\activate  # En Windows
   pip install -r requirements.txt
   ```

3. Configura la base de datos MySQL:
   - Crea una base de datos llamada `clinicas` en MySQL
   - Asegúrate de que las credenciales en `Config/settings.py` coincidan con tu configuración local:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': 'clinicas',
             'USER': 'root',
             'PASSWORD': '',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

4. Aplica las migraciones:
   ```
   python manage.py migrate
   ```

5. Crea un superusuario para acceder al panel de administración:
   ```
   python manage.py createsuperuser
   ```

6. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

7. Accede al panel de administración en `http://localhost:8000/admin/` e inicia sesión con el superusuario creado.

## Uso del Sistema

### Administración de Clínicas
1. Accede al panel de administración
2. Crea una o más clínicas desde la sección "Clínicas"

### Configuración de Ubicaciones (Ubigeo)
1. Crea ubicaciones geográficas (departamento, provincia, distrito) asociadas a cada clínica

### Registro de Pacientes
1. Registra pacientes asociados a una clínica específica
2. Asigna la ubicación geográfica correspondiente al paciente

### Gestión de Citas
1. Programa citas para los pacientes
2. Actualiza el estado de las citas según corresponda (programada, confirmada, atendida, cancelada)

## Relaciones entre Modelos

- Cada clínica puede tener múltiples ubicaciones geográficas (ubigeos)
- Cada clínica puede tener múltiples pacientes
- Cada paciente pertenece a una clínica y puede tener una ubicación geográfica
- Cada cita está asociada a una clínica y a un paciente, y puede tener una ubicación específica

## Consideraciones Importantes

- El sistema está diseñado para manejar múltiples clínicas, cada una con sus propios pacientes, citas y ubicaciones
- Las ubicaciones geográficas (ubigeos) están vinculadas a clínicas específicas
- Los pacientes solo pueden tener ubicaciones geográficas que pertenezcan a su misma clínica


Consideraciones Importantes
El sistema está diseñado para manejar múltiples clínicas, cada una con sus propios pacientes, citas y ubicaciones
Las ubicaciones geográficas (ubigeos) están vinculadas a clínicas específicas
Los pacientes solo pueden tener ubicaciones geográficas que pertenezcan a su misma clínica
