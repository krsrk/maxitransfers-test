
# Maxitransfers Test

## Prerrequisitos

- Tener Docker y Docker Compose instalado
- Tener instalado WSL2 y Ubuntu 20.04 si se va a ejecutar en Windows

## Instalación

### Docker

#### 1.- Construir las imagenes(navegar al directorio raíz del proyecto)

```bash
> docker compose build
```


#### 2.- Levantar los servicios
```bash
> docker compose up -d
```

#### 3.- Se puede verificar el estado de los servicios
```bash
> docker compose ps
```

### Base de Datos

#### 1.- Inicializar la base de datos
```bash
> docker compose exec -it db /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 's8s!Np#m76LV#iN' -i init.sql
```

### Server (Front-End)

#### 1.- Instalar las dependencias
```bash
docker compose exec -it front npm install
```

#### 2.- Iniciar el server
```bash
> docker compose exec -it front npm run dev
```

#### 3.- Probar la app en la siguiente url: http://localhost:3001


## API (Back-End)
#### Base Url: http://localhost:8089/api

#### Servicio de Empleados
    Obtener empleados: /employees  (GET) 
    
    Crear empleado:    /employee   (POST) 
        Body: JSON 
        {
            "name": "Ace D.",
            "last_name": "Portgas",
            "birth_date": "2000-01-01",
            "employee_number": "A0101",
            "curp": "VLC800409HASC",
            "ssn": "78787878787878",
            "phone_number": "44918786690",
            "nationality": "Mexicana"
        }
    
    Actualizar Empleado: /employee   (PUT)
        Body: JSON
        {
            "employee_id": 8, 
            "name": "Don Quixote",
            "last_name": "DoFlamingo",
            "birth_date": "2000-01-01",
            "employee_number": "A0103",
            "curp": "VLC800409HASC",
            "ssn": "78787878787878",
            "phone_number": "44918786690",
            "nationality": "Mexicana"
        }
    
    Borrar Empleado: /employee   (DELETE)
        Body: JSON
        {
            "employee_id": 3
        }

#### Servicio de Beneficiarios

    Obtener beneficiarios: /beneficiaries/employee/{id_empleado}  (GET) 
    
    Crear beneficiario:    /beneficiaries/employee/{id_empleado}  (POST) 
        Body: JSON 
        {
            "name": "Water",
            "last_name": "Trafalgar D.",
            "birth_date": "2000-01-01",
            "curp": "VLC800409HASC",
            "ssn": "78787878787878",
            "phone_number": "44918786690",
            "nationality": "Mexicana",
            "participation_percentage": 10
        }
    
    Actualizar Empleado: /beneficiaries   (PUT)
        Body: JSON
        {
            "beneficiary_id": 8,
            "name": "Water",
            "last_name": "Trafalgar D.",
            "birth_date": "2000-01-02",
            "curp": "VLC800409HASC",
            "ssn": "78787878787878",
            "phone_number": "44918786690",
            "nationality": "Mexicana",
            "participation_percentage": 8
        }
    
    Borrar Empleado: /beneficiaries   (DELETE)
        Body: JSON
        {
            "beneficiary_id": 8
        }



## Directorios

    /infra: donde se encuentran los Dockerfiles de los servicios
        /back
        /front

    /src: código fuente de las aplicaciones
        /back: código base Flask Python
        /front: código base Vue Js Nuxt

    /volumes: volumenes compartidos para las base de datos y el script de inicialización de la base de datos.



