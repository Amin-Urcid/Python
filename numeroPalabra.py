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
        prefijo = "mil" if miles == 1 else numero_a_palabras(miles) + " mil"
        return prefijo + (" " + numero_a_palabras(resto) if resto != 0 else "")
    elif n < 1_000_000_000:
        millones = n // 1_000_000
        resto = n % 1_000_000
        prefijo = "un millón" if millones == 1 else numero_a_palabras(millones) + " millones"
        return prefijo + (" " + numero_a_palabras(resto) if resto != 0 else "")
    else:
        return "Número demasiado grande (máximo 999,999,999)"


def decimal_a_palabras(numero_str):
    # Separar parte entera y decimal usando punto o coma
    numero_str = numero_str.replace(",", ".")

    if "." in numero_str:
        partes = numero_str.split(".")
        parte_entera = int(partes[0])
        parte_decimal_str = partes[1]

        # Convertir parte entera
        resultado = numero_a_palabras(abs(parte_entera))
        if parte_entera < 0:
            resultado = "menos " + resultado

        # Convertir parte decimal dígito por dígito
        digitos = ["cero", "uno", "dos", "tres", "cuatro",
                   "cinco", "seis", "siete", "ocho", "nueve"]
        decimales_palabras = " ".join(digitos[int(d)] for d in parte_decimal_str)

        resultado += " punto " + decimales_palabras
        return resultado
    else:
        numero = int(numero_str)
        return numero_a_palabras(numero)


# Programa principal
while True:
    entrada = input("\nEscribe un número (o 'salir' para terminar): ").strip()
    if entrada.lower() == "salir":
        print("¡Hasta luego!")
        break
    try:
        # Validar que sea un número válido
        float(entrada.replace(",", "."))
        print(f"En palabras: {decimal_a_palabras(entrada)}")
    except ValueError:
        print("Por favor, ingresa un número válido.")
        
'''        

**¿Qué se agregó?**

- Soporte para **números decimales**, usando tanto punto (`.`) como coma (`,`) como separador.
- La parte decimal se lee **dígito por dígito**, tal como se hace normalmente en español.
- Funciona también con números negativos decimales.

**Ejemplo de salida:**

Escribe un número (o 'salir' para terminar): 3.14
En palabras: tres punto uno cuatro

Escribe un número (o 'salir' para terminar): -1500,75
En palabras: menos mil quinientos punto siete cinco

Escribe un número (o 'salir' para terminar): 1000000
En palabras: un millón

'''
