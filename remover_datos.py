def remover_datos(archivo):
        arch = open(archivo, "r")
        registros = arch.readlines()
        count=0
        for reg in registros:
            lista = reg.split(",")
            count+=1
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            espacios = " " * (18 - (len(lista[0])))
            ren = str(count)+ lista[0] + espacios 
            espacios = " " * (28 - (len(lista[1])))
            ren += str(count)+ lista[1] + espacios
            espacios = " " * (25 - (len(lista[2])))
            ren += str(count)+ lista[2] + espacios
            espacios = " " * (27 - (len(lista[3])))
            ren += str(count)+ lista[3] + espacios
            espacios = " " * (47 - (len(lista[4])))
            ren += str(count)+ lista[4] + espacios
            ren += " " + str(count)+  lista[5]
            print(ren, end="")
        
        fila = int(input("Ingrese el registro que desea borrar ?"))
        filebuffer = ""
        countRows = 0  
        print("Imprimimos listas: ")
        for reg in registros:
            lista = reg.split(",")
            countRows+=1
            print(countRows)
            print(lista)
            if countRows == fila:
                print(f"Fila eliminada : {lista}")
            else:
                countcamp =  0 
                for campo in lista:
                    countcamp +=1 
                    if countcamp == 6 or countcamp ==1: 
                        print("acción terminada")
                    else:
                        filebuffer += ","
                    
                    filebuffer += campo 
                    countcamp +=1                                   
    
        arch = open(archivo, "w")
        arch.write(filebuffer)
        arch.close()
        
        