# Calculadora de Propinas

Programa interactivo en Python que calcula la propina y el total a pagar de una cuenta, según el porcentaje que indique el usuario.

**Ruta:** Python & Data Science — Fase 1, Proyecto 1
**Nivel:** Principiante absoluto
**Tiempo estimado:** 30–60 minutos

## Objetivo

Construir un programa que pida al usuario el total de una cuenta y un porcentaje de propina, y muestre cuánto debe dejar de propina y el total final a pagar.

## Requisitos previos

- Python instalado, o
- Cuenta en Google Colab

## Cómo ejecutar

```bash
python calculadora_propinas.py
```

## Ejemplo de uso

```
=== Calculadora de Propinas ===
Ingresa el total de tu cuenta: 85000
Ingresa el porcentaje de propina (ej: 10): 15
--- Resultado ---
Propina (15%): $12,750.00
Total a pagar: $97,750.00
```

## Requisitos funcionales

| ID | Descripción |
|----|-------------|
| RF-1 | Muestra el título `=== Calculadora de Propinas ===` al iniciar. |
| RF-2 | Pide al usuario el total de la cuenta. |
| RF-3 | Pide al usuario el porcentaje de propina. |
| RF-4 | Calcula la propina en pesos. |
| RF-5 | Calcula el total final (cuenta + propina). |
| RF-6 | Muestra los resultados con 2 decimales, signo `$` y separador de miles. |
| RF-7 | El código está en un archivo `calculadora_propinas.py` o notebook. |

## Conceptos usados

- **Input**: lectura de datos escritos por el usuario en consola.
- **Output**: impresión de texto y resultados en consola.
- **Variables**: almacenamiento de los valores ingresados y calculados.
- **Tipos de dato**: diferencia entre texto (`string`) y número (`int`, `float`).
- **Conversión de tipos**: transformar la entrada de texto a número.
- **Operadores aritméticos**: suma y multiplicación para calcular propina y total.
- **Formato de números**: presentación con 2 decimales y separador de miles.

## Criterios de éxito

- El programa corre sin errores.
- La salida coincide exactamente con los ejemplos de este README.
- El código puede explicarse línea por línea.
- El programa puede modificarse ante nuevos requerimientos.
