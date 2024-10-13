def mostrar_repositorio(archivo):
    arch = open(archivo, "r")
    for reg in arch.readlines():
        lista = reg.split(",")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        espacios = " " * (18 - (len(lista[0])))
        ren = lista[0] + espacios
        espacios = " " * (28 - (len(lista[1])))
        ren += lista[1] + espacios
        espacios = " " * (25 - (len(lista[2])))
        ren += lista[2] + espacios
        espacios = " " * (27 - (len(lista[3])))
        ren += lista[3] + espacios
        espacios = " " * (47 - (len(lista[4])))
        ren += lista[4] + espacios
        ren += " " + lista[5]
        print(ren, end="")
        
        