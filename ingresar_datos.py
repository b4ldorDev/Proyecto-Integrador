def ingresar_datos(archivo):
    levelType = input("Ingrese el levelType: ")
    code = input("Ingrese el code:  ")
    catalogType = input("Ingrese el catalogType:  ")
    name = input("Ingrese el name : ")
    description = input("Ingrese la descripción: ")
    sourceLink = input("Ingrese el sourceLink")
    nuevo_registro = levelType + "," + code + "," + catalogType + "," + name + "," + description + "," + sourceLink + "\n"
    arch = open(archivo, "a")
    arch.write(nuevo_registro)
    arch.close()
    return archivo