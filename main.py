import os  
import funciones
csv="catalog_v2.csv"
def ingresar_datos(archivo):
#Los datos se deben cargar como listas
    levelType=input("Ingrese el levelType: ")
    code=input("Ingrese el code:  ")
    catalogType=input("Ingrese el catalogType:  ")
    name=input("Ingrese el name : ")
    description=input("Ingrese la descripción: ")
    sourceLink=input("Ingrese el sourceLink")

    nuevo_registro=levelType+","+code+","+catalogType+","+name+","+description+","+sourceLink+"\n"
    arch=open(archivo,"+a")
    arch.write(nuevo_registro)
    arch.close()
    return archivo

def remover_datos(archivo):
    
    pass
 
def modificar_datos(archivo):
    pass 



def mostrar_repositorio(archivo):
    #|----------|--------------------|----------|------------------------------|----------------------------------------------|---------------------------------------------|
    arch=open(archivo,"r")
    #print("|levelType|       |code|       |catalogType|       |  name  |       |description|       |sourceLink|")
    #                 1234567      1234567             1234567          1234567             1234576
    #      12345678912       123456       1234567891234       1234567891       1234567891234       123456789123
    for reg in arch.readlines():
        lista=reg.split(",")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        espacios=" "*(18-(len(lista[0])))
        ren=lista[0]+espacios
        espacios=" "*(28-(len(lista[1])))            
        ren+=lista[1]+espacios
        espacios=" "*(25-(len(lista[2])))                       
        ren+=lista[2]+espacios
        espacios=" "*(27-(len(lista[3])))                                   
        ren+=lista[3]+espacios
        espacios=" "*(47-(len(lista[4])))                                   
        ren+=lista[4]+espacios
           # espacios=" "*(2-len(lista[6]))                                   
        ren+=" "+lista[5] 
        print(ren, end="")
        

def consultar_datos(archivo):
    op = int(input(" Ingresa el numero del valor que tiene: \n1) levelType \n 2)  code  \n  3) catalogType  \n 4) name  \n 5) description  \n  6) sourceLink \n"))
    code = input("Ingresa el codigo:  ")
    arreglo=[]
    arch=open(archivo,"r")
    for reg in arch.readlines():
        lista=reg.split(",")
        if lista[(op-1)]==code:
            arreglo.append(lista)
    if len(arreglo) ==0: 
        print("No existe o hubo un error al introducir el codigo")
    else:
        print("|levelType|  |code|       |catalogType|  |  name  |   |description|   |sourceLink|")
        #      12345678912  123456       1234567891234  1234567891 1234567891234 123456789123
        print("-------------------------------------------------------------------------------")
        for linea in arreglo:
            espacios=" "*(18-(len(lista[0])))
            ren=linea[0]+espacios
            espacios=" "*(28-(len(lista[1])))            
            ren+=linea[1]+espacios
            espacios=" "*(25-(len(lista[2])))                       
            ren+=linea[2]+espacios
            espacios=" "*(27-(len(lista[3])))                                   
            ren+=linea[3]+espacios
            espacios=" "*(47-(len(lista[4])))                                   
            ren+=linea[4]+espacios
           # espacios=" "*(2-len(lista[6]))                                   
            ren+=linea[5] 
            print(ren, end="")
        
def analisis_de_datos():
    pass    

def menu():
    op=int(input("A.    Mostrar el detalle del repositorio. \n",
        "B.    Buscar un registro de datos. \n",
        "C.    Consulta un conjunto de registros. \n",
        "D.    Modificar data existente.\n",
        "E.    Ingresar un nuevo registro de datos.\n",
        "F.    Remover un registro de datos existente.\n",
        "G.    Finalizar."))

    if op==chr(75) or op==chr(97): 
        mostrar_repositorio(csv)    
    if op==chr(66) or op==chr(98):
        consultar_datos(csv)
    if op==chr(67) or op==chr(99): 
        modificar_datos(csv)        
    if op==chr(68) or op==chr(100):
        modificar_datos(csv)
    if op==chr(69) or op==chr(101):            
        ingresar_datos(csv)
    if op==chr(70) or op==chr(102):
        remover_datos(csv)
    if op==chr(71) or op==chr(103):
        return False
                
#Función para inicializar
def main():
    consultar_datos(csv)

if __name__ == "__main__":
        main()