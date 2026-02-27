#Este programa transforma en palabras el numero que escriba el usuario.

def numero_a_palabras(n):
    if n < 0:
        return "menos " + numero_a_palabras(-n)

    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve",
                "diez", "once", "doce", "trece", "catorce", "quince", "dieciséis", "diecisiete",
                "dieciocho", "diecinueve"]

    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]

    centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos",
                "seiscientos", "setecientos", "ochocientos", "novecientos"]

    if n == 0:
        return "cero"
    elif n < 20:
        return unidades[n]
    elif n < 100:
        if n == 20:
            return "veinte"
        elif n < 30:
            return "veinti" + unidades[n - 20]
        else:
            resto = n % 10
            return decenas[n // 10] + (" y " + unidades[resto] if resto != 0 else "")
    elif n < 1000:
        if n == 100:
            return "cien"
        resto = n % 100
        return centenas[n // 100] + (" " + numero_a_palabras(resto) if resto != 0 else "")
    elif n < 1_000_000:
        miles = n // 1000
        resto = n % 1000
        if miles == 1:
            prefijo = "mil"
        else:
            prefijo = numero_a_palabras(miles) + " mil"
        return prefijo + (" " + numero_a_palabras(resto) if resto != 0 else "")
    elif n < 1_000_000_000:
        millones = n // 1_000_000
        resto = n % 1_000_000
        if millones == 1:
            prefijo = "un millón"
        else:
            prefijo = numero_a_palabras(millones) + " millones"
        return prefijo + (" " + numero_a_palabras(resto) if resto != 0 else "")
    else:
        return "Número demasiado grande (máximo 999,999,999)"


# Programa principal
while True:
    entrada = input("\nEscribe un número entero (o 'salir' para terminar): ")
    if entrada.lower() == "salir":
        print("¡Hasta luego!")
        break
    try:
        numero = int(entrada)
        print(f"En palabras: {numero_a_palabras(numero)}")
    except ValueError:
        print("Por favor, ingresa un número entero válido.")
        
'''
**¿Qué hace el programa?**

- Convierte números enteros a palabras en **español**.
- Soporta números **negativos**.
- Maneja rangos desde cero hasta **999,999,999**.
- Tiene un bucle para que puedas convertir varios números sin reiniciar.
- Valida que la entrada sea un número válido.

**Ejemplo de salida:**

Escribe un número entero (o 'salir' para terminar): 1542
En palabras: mil quinientos cuarenta y dos

Escribe un número entero (o 'salir' para terminar): -305
En palabras: menos trescientos cinco

'''
