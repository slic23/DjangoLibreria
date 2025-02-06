#!/bin/bash

set -e  # Salir inmediatamente si un comando sale con un estado de error

# Instalación de requerimientos
echo "Instalando requerimientos..."
if [ -f requirements.txt ]; then
    pip3 install -r requirements.txt
else
    echo "Error: requirements.txt no encontrado."
    exit 1
fi

# Migraciones automáticas
echo "Iniciando migraciones..."
if python3 manage.py makemigrations; then
    echo "makemigrations se ejecutó correctamente."
else
    echo "Error al ejecutar makemigrations."
    exit 1
fi

if python3 manage.py migrate; then
    echo "migrate se ejecutó correctamente."
else
    echo "Error al ejecutar migrate."
    exit 1
fi

# Recolección de archivos estáticos
echo "Colectando StaticFiles..."
if python3 manage.py collectstatic --noinput; then
    echo "collectstatic se ejecutó correctamente."
else
    echo "Error al ejecutar collectstatic."
    exit 1
fi
