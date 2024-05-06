def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        else:
            return True
    else:
        return True

while True:
    try:
        value = int(input("Ingrese un número natural: "))
        if value > 0:
            print("Los números primos del 1 al",value ,"son...")
            for i in range(1, value+1):
                if is_prime(i + 1):
                    print(i + 1, end=" ")
        else:
            print("Error. El valor debe ser positivo mayor a 0")
        salir = input("\n¿Desea salir? Escriba \"si\"\n")
        if salir == "si":
            break
    except(ValueError):
        print("Error. El valor ingresado no es un número")