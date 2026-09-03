# ============================================
# CALCULADORA - Funciones adicionales
# Agreguen estas funciones a su calculadora.py,
# una por una, con su propio commit para cada una
# ============================================

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: no existe raiz de un numero negativo"
    return numero ** 0.5