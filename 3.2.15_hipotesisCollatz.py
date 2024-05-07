
while True:
    try:
        c0 = input("Ingrese un número, o escriba \"salir\": ")
        if c0 == "salir":
            break
        c0 = int(c0)
        pasos = 0

        while (c0 > 0):
            if c0 % 2 == 0:
                c0 = int(c0 / 2)
                print(c0)
                pasos += 1
            else:
                c0 = int(3 * c0 + 1)
                print(c0)
                pasos += 1
            if c0 == 1:
                break
            
        print("Pasos =", pasos)

    except(ValueError):
        print("Ingresa un número entero")
    except():
        print("Ingresa un número entero")  