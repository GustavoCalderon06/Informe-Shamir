# Informe-Shamir

Guía de Instalación y Uso
Requisitos
Python 3.x
SymPy (instalable con pip install sympy)
Instalación
Instalar Python 3: Asegúrate de tener Python instalado. Puedes descargarlo desde python.org.
Instalar dependencias: Ejecuta en la terminal:
bash
Copiar código
pip install sympy
Uso del Código
Ejecuta el código para generar y dividir un secreto en partes.
Generación de Partes: El código dividirá el secreto en n partes y te mostrará las partes generadas.
Reconstrucción del Secreto: Utiliza un subconjunto de t partes para reconstruir el secreto. Si alguna parte es modificada, el sistema fallará en la reconstrucción, tal como está demostrado en la sección de pruebas del código.
