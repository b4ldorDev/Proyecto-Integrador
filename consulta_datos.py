def consulta_datos(archivo):
    op = int(input(
        " Ingresa el numero del valor que tiene: \n1) levelType \n 2)  code  \n  3) catalogType  \n 4) name  \n 5) description  \n  6) sourceLink \n"))
    code = input("Ingresa el codigo:  ")
    arreglo = []
    arch = open(archivo, "r")
    for reg in arch.readlines():
        lista = reg.split(",")
        if lista[(op - 1)] == code:
            arreglo.append(lista)
    if len(arreglo) == 0:
        print("No existe ")
    else:
        print("|levelType|  |code|       |catalogType|  |  name  |   |description|   |sourceLink|")
        print("-------------------------------------------------------------------------------")
        for linea in arreglo:
            espacios = " " * (18 - (len(lista[0])))
            ren = linea[0] + espacios
            espacios = " " * (28 - (len(lista[1])))
            ren += linea[1] + espacios
            espacios = " " * (25 - (len(lista[2])))
            ren += linea[2] + espacios
            espacios = " " * (27 - (len(lista[3])))
            ren += linea[3] + espacios
            espacios = " " * (47 - (len(lista[4])))
            ren += linea[4] + espacios
            ren += linea[5]
            print(ren, end="")
        #Recorrido comprobar registrOs
        nullCount = [0] * 6
        qnttyCampos = len(arreglo[0])
        qnttyRegistros = len(arch.readlines()) -1
        for registro in arreglo:
          for campo in registro:
            if(campo == None or len(campo) == 0):
              nullCount[registro.index(campo)] +=1
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f" La distribución de espacios vacios en el registro de 6 campos es  {nullCount}")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(f"Contiene {qnttyCampos-1} campos ")
