
while True:
    try:
        blocks = input("Ingresa el número de bloques, o escriba \"salir\": ")
        if blocks == "salir":
            break
        blocks = int(blocks)
        suma = 0
        height = 0

        for i in range(1, blocks + 1):
            if suma + i == blocks:
                height += 1
                break
            elif suma + i > blocks:
                break
            else:
                suma += i
                height += 1
            
        print("La altura de la pirámide:", height, "\n")
        
    except(ValueError):
        print("Ingresa un número entero")
    except():
        print("Ingresa un número entero")