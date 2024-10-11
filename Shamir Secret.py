import random
from sympy import symbols, Eq, solve

# Genera un polinomio de grado t-1
def generar_polinomio(secreto, t, primo):
    coeficientes = [secreto] + [random.randint(1, primo-1) for _ in range(t-1)]
    return coeficientes

# Evalúa el polinomio en un valor de x
def evaluar_polinomio(coeficientes, x, primo):
    resultado = 0
    for i, coef in enumerate(coeficientes):
        resultado += coef * (x ** i)
    return resultado % primo

# Genera las partes del secreto (x, y)
def generar_partes(secreto, n, t, primo):
    coeficientes = generar_polinomio(secreto, t, primo)
    partes = []
    for i in range(1, n + 1):
        partes.append((i, evaluar_polinomio(coeficientes, i, primo)))
    return partes

# Interpolación de Lagrange para reconstruir el secreto
def reconstruir_secreto(partes, primo, secreto_original):
    # Verificar si hay suficientes partes para la reconstrucción
    if len(partes) < t:
        raise ValueError("No hay suficientes partes para reconstruir el secreto.")
    
    secreto = 0
    for i, (x_i, y_i) in enumerate(partes):
        numerador, denominador = 1, 1
        for j, (x_j, _) in enumerate(partes):
            if i != j:
                numerador = (numerador * (-x_j)) % primo
                denominador = (denominador * (x_i - x_j)) % primo
        lagrange_coef = numerador * pow(denominador, -1, primo)
        secreto = (secreto + y_i * lagrange_coef) % primo

    # Comprobar si el secreto reconstruido coincide con el secreto original
    if secreto != secreto_original:
        raise ValueError("El secreto reconstruido no coincide con el secreto original, indicando una modificación.")

    return secreto

# Parámetros
primo = 2087  # Un número primo grande
secreto = 1234  # El secreto a compartir
n = 5  # Número total de partes
t = 3  # Umbral para la reconstrucción

# Generar las partes del secreto
partes = generar_partes(secreto, n, t, primo)
print("Partes generadas:")
for parte in partes:
    print(f"Parte {parte[0]}: {parte[1]}")

# Seleccionar un subconjunto de partes (t partes) y reconstruir el secreto
partes_seleccionadas = partes[:t]
secreto_reconstruido = reconstruir_secreto(partes_seleccionadas, primo, secreto)
print(f"\nSecreto reconstruido: {secreto_reconstruido}")




# Sección de pruebas

# Seleccionar las primeras 3 partes y reconstruir el secreto
partes_minimas = partes[:3]
secreto_reconstruido = reconstruir_secreto(partes_minimas, primo, secreto)
print(f"Secreto reconstruido con 3 partes: {secreto_reconstruido}")

# Intentar reconstruir el secreto con solo 2 partes (esto debería fallar)
partes_insuficientes = partes[:2]
try:
    secreto_reconstruido = reconstruir_secreto(partes_insuficientes, primo, secreto)
    print(f"Secreto reconstruido con 2 partes: {secreto_reconstruido}")
except Exception as e:
    print("No se pudo reconstruir el secreto con menos de 3 partes, como era esperado.")

# Modificar una de las partes y tratar de reconstruir el secreto
partes_modificadas = partes[:3]
partes_modificadas[0] = (partes_modificadas[0][0], partes_modificadas[0][1] + 1)  # Alterar la primera parte
try:
    secreto_reconstruido = reconstruir_secreto(partes_modificadas, primo, secreto)  # Usar el secreto original
    print(f"Secreto reconstruido con partes modificadas: {secreto_reconstruido}")
except Exception as e:
    print("El sistema falló al reconstruir el secreto con partes modificadas, como era esperado.")


