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
    #Mostr
    pass
 
def modificar_datos(archivo):
    pass 
                
def mostrar_repositorio(archivo):
    arreglo = funciones.csv_a_arreglo(archivo)       
    
    for fila in arreglo:
        print()
        

def consultar_datos(archivo):
    consulta_usuario=input("locations.locationIdentifier: ")
    arch=open(archivo,"r")
    existencia=False
    for elemento in arch.readlines():# leemos cada linea del archivo      
        lista=elemento.split(",")
        if lista[1]==consulta_usuario:
            existencia=True
            print(f"levelType: {lista[0]} \n code:  {lista[1]} \n catologType :  {lista[2]} \n name: {lista[3]} \n description: {lista[4]} \n sourceLink: {lista[5]}")
            break
        
    if existencia != True:
        print("No existe el articulo o el código puede ser erroneo,| vuelva a escribir")
    
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
              
def csv_a_arreglo():
    arreglo=[]
    arch=open(archivo,"r")
    for reg in arch.readlines():
        columna = [1]
        lista=reg.split(",")
        for elemento in lista:
            columna.append(elemento)
        arreglo.append(columna)
                
#Función para inicializar
def main():

    mostrar_repositorio(csv)    


if __name__ == "__main__":
        main()