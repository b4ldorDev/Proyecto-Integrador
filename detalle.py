def detalle_del_repo(archivo):
    count_rows= 0
    count_cols = 0
    arch = open(archivo, "r")
    for reg in arch.readlines():
        count_rows +=1
        lista = reg.split(",")
        for elemento in lista:
            count_cols +=1
    print("Numero de columnas del repositorio es  ", ((count_cols//count_rows)))
    print("Numero de registros del repositorio es ", count_rows)
    

