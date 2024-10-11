# Informe-Shamir

Guía de Instalación y Uso

## Requisitos del Sistema
- Python 3.x
- Paquete SymPy para operaciones algebraicas

## Instalación
- Instalar Python 3.x: Si no tienes Python instalado, descárgalo e instálalo desde python.org.
- Instalar SymPy: Ejecuta el siguiente comando en la terminal o en el CMD para instalar la biblioteca SymPy:
-  ```bash
  pip install sympy

## Uso del Código
- Ejecuta el código para generar y dividir un secreto en partes.
- Generación de Partes: El código dividirá el secreto en n partes y te mostrará las partes generadas.
- Reconstrucción del Secreto: Utiliza un subconjunto de t partes para reconstruir el secreto. Si alguna parte es modificada, el sistema fallará en la reconstrucción, tal como está demostrado en la sección de pruebas del código.
