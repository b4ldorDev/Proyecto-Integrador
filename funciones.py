def tipo_dato(cadena):
    especiales=[]
    num = [x for x in cadena if x.isnumeric() == True]
    alpha = [x for x in cadena if x.isalpha() == True]
    alphanumeric = [x for x in cadena if x.isalnum() == True]
    especiales = [x for x in cadena if x.isalnum() == False and x.isnumeric==False and x.isalpha()== False]

    if (num==0 and alpha ==0 and alphanumeric==0 and especiales==0 ):
        print("Los datos son nulos")
    if len(cadena) == len(num):
        print("Todos los caracteres son numeros:")
    if len(cadena) == len(alpha):
        print("Todos los caracteres son alfabeticos:")
    if len(cadena) == len(alphanumeric):
        print("Todos los caracteres son alfanumericos:")
    if len(cadena) == len(especiales):
        print("Todos los caracteres son especiales ")
    else:              
        print(f"No todos los caracteres son números solo contiene {len(num)} y son {num}")
        print(f"No todos los caracteres son números solo contiene {len(alpha)} y son {alpha}")
        print(f"No todos los caracteres son números solo contiene {len(alphanumeric)} y son {alphanumeric}")
        print(f"No todos los caracters son especiales solo contiene {len(especiales)} y son {especiales}")

def csv_a_arreglo(archivo):
    arreglo=[]
    arch=open(archivo,"r")
    for reg in arch.readlines():
        columna = [1]
        lista=reg.split(",")
        for elemento in lista:
            columna.append(elemento)
        arreglo.append(columna) 
    return arreglo   
        
#def cantidad_de_campos():

#def cantidad_de_registros():

#def existencia():
    