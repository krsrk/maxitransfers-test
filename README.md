
# Maxitransfers Test

## Prerrequisitos

```bash
- Tener Docker y Docker Compose instalado
- Tener instalado WSL2 y Ubuntu 20.04 si se va a ejecutar en Windows
```

## Instalación

### Docker
```bash
1.- Construir las imagenes(navegar al directorio raíz del proyecto)

> docker compose build

2.- Levantar los servicios

> docker compose up -d

3.- Se puede verificar el estado de los servicios

> docker compose ps
```

### Base de Datos

```bash
1.- Inicializar la base de datos

> docker compose exec -it db /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P 's8s!Np#m76LV#iN' -i init.sql

```

### Server(Front)

```bash
1.- Instalar las dependencias

> docker compose exec -it front npm install

2.- Iniciar el server

> docker compose exec -it front npm run dev

3.- Probar la app en la siguiente url: http://localhost:3001

```

## Directorios

```bash
/infra: donde se encuentran los Dockerfiles de los servicios
   /back
   /front

/src: código fuente de las aplicaciones
   /back: código base Flask Python
   /front: código base Vue Js Nuxt

/volumes: volumenes compartidos para las base de datos y el script de inicialización de la base de datos.
```
