#!/bin/bash

set -e  # Salir inmediatamente si un comando sale con un estado de error

# Instalación de pip
echo "Instalando pip..."
if command -v pip3 &> /dev/null; then
    echo "pip3 ya está instalado."
else
    echo "pip3 no encontrado. Instalando..."
    if command -v python3 &> /dev/null; then
        python3 -m ensurepip --upgrade
    elif command -v python &> /dev/null; then
        python -m ensurepip --upgrade
    else
        echo "Python no encontrado. Instala Python manualmente."
        exit 1
    fi
fi

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
