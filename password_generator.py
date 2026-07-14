import random
import string

def main():
    print("=== Generador de Contraseñas ===")
    print("")
    # pide al usuario la cantidad de caracteres usando una función validadora de enteros
    char_amount = int_validator()
    print("")
    # colección de caracteres usando el módulo string
    string_pool = (string.ascii_letters + string.digits + string.punctuation)
    # lista vacía de caracteres de la contraseña
    password_list = []
    
    # añade un caracter aleatorio a la lista usando el modulo random e itera x cantidad de veces según cantidad de caracteres digitados por el usuario
    for _ in range(char_amount):
        password_list.append(random.choice(string_pool))
    
    # convierte la lista de caracteres en un solo string
    password = "".join(password_list)
    print("--- Resultado ---")
    print(f"Tu contraseña generada es: {password}")

# función que valida que el valor digitado por el usuario sea entero positivo mayor a cero
def int_validator():
    error_message = "Digita un número entero positivo mayor a cero"
    while True:
        try:
            number = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? "))
            if number > 0:
                return number
            else:
                print(error_message)
        except:
            print(error_message)

if __name__ == "__main__":
    main()
