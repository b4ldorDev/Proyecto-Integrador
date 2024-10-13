#Importamos las librerias que creamos anteriormente para cada una de las opciones del programa
#El separarlas en funciones y usarlas como metodos nos ayuda a mantener un orden en el código
import detalle as dr  # importamos el archivo 
import mostrar_datos as vd #
import consulta_datos as cd #
import busca_datos as bd #
import modificar_datos as md #
import ingresar_datos as sd #
import remover_datos as rd #

#Importamos el archivo y lo guardamos en una variable  
data= "catalog_v2.csv"

def menu():
    # Utilizamos las comillas tripes en el menu para poder escribir un solo input en distintas lineas 
    # Usamos los \n para los saltos de linea en cada opción 
    op = (input('''\n
                   A.    Mostrar el detalle del repositorio. \n
                   B.    Buscar un registro de datos. \n
                   C.    Consulta un conjunto de registros. \n
                   D.    Modificar data existente.\n
                   E.    Ingresar un nuevo registro de datos.\n
                   F.    Remover un registro de datos existente.\n
                   G.    Finalizar.'''))

#Opción A) 
    # 
    if op == "a" or op == "A":
        dr.detalle_del_repo(data) 
        view  = input(f"Desea ver el repositorio completo ? \n  Y) si \n N) no ")
        #Usamos el código ASCII para detectar la opción en minuscula y mayuscula 
        if view == chr(121) or view == (89):
            vd.mostrar_repositorio(data)
        else:
            print("Función finalizada \n")
#Opción B)                        
    if op == "b" or op == "B":
        print("Buscar  Datos \n")
        bd.busca_datos(data)             
        print("Función finalizada \n")        
#Opción C)            
    if op == "c" or op == "C":
        print("Consultar Datos \n")
        cd.consulta_datos(data)             
        print("Función finalizada \n")
#Opción D) 
    if op == "d" or op == "D":
        print("Modificar Datos \n")
        md.modificar_datos(data)
        print("Función finalizada \n")
#Opción E) 
    if op == "e" or op == "E" :
        print("Ingresar Datos del repositorio \n")
        sd.ingresar_datos(data)
        print("Función finalizada \n")                
#Opción F) 
    if op == "f" or op == "F":
        print("Remover Datos \n")
        rd.remover_datos(data)
        print("Función finalizada \n")                
#Opción) G)
    if op == "g" or op == "G":
        return False
    
def main():
    #Debido a que no podemos usar break cuando el menu retorne False terminara el bucle 
    while menu() !=False:
        menu()
    
if __name__ == "__main__":
    main()