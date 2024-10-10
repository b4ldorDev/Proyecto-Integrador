def modificar_datos(archivo):
    op = int(input(
        " Ingresa el numero del valor que tiene: \n1) levelType \n 2)  code  \n  3) catalogType  \n 4) name  \n 5) description  \n  6) sourceLink \n"))
    code = input("Ingresa el codigo:  ")
    arreglo = []
    arch = open(archivo, "r")
    registros = arch.readlines()
    for reg in registros:
        lista = reg.split(",")
        if lista[(op - 1)] == code:
            arreglo.append(lista)
    if len(arreglo) == 0:
        print("No existe o hubo un error al introducir el codigo")
    else:
        print(" # |levelType|  |code|       |catalogType|  |  name  |   |description|   |sourceLink|")
        print("-------------------------------------------------------------------------------")
        cont = 0
        for linea in arreglo:
            cont += 1
            # TODO: Mostrar su numero
            espacios = " " * (18 - (len(lista[0])))
            ren = str(cont) + " " + linea[0] + espacios
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
        # TODO: Verificar que este rango
        fila = int(input("Cual Registro Desea Modificar?"))
        numCampo = int(input(" Ingresa el numero del campo a modificar: \n1) levelType \n 2)  code  \n  3) catalogType  \n 4) name  \n 5) description  \n  6) sourceLink \n"))
        # Comprobacion Correcta
        fila -= 1
        modCampo = input("Con que se va a sustituir: ")
        filebuffer = ""
        for reg in registros:
            lista = reg.split(",")
            if lista[(op - 1)] == code:
                if fila != 0:
                  fila -= 1
                  filebuffer += reg
                else:
                  lista[numCampo-1] = modCampo
                  isFirst = True
                  count=0 
                  for campo in lista:
                    count+=1
                    if count == len(lista):
                        filebuffer += campo
                        break
                    if not isFirst: 
                      isFirst = False
                      filebuffer += ","
                    filebuffer += campo+ ","
                    
                  fila -= 1
            else:
                filebuffer += reg  
        arch = open(archivo, "w")
        arch.write(filebuffer)
        arch.close()
