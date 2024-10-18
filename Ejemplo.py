#Examen Final Pensamiento computaciónal :P 

import time 
inicio = time.time()
time.sleep(1)
def sacar_palabras(archivo):
    arch =open(archivo,"r")
    lista_de_palabras=[]
    for renglon in arch.readlines():
        lista= renglon.split(" ")
        for palabra in lista:
            lista_de_palabras.append(palabra)
    arch.close()
    return lista_de_palabras
    
def mezcla(ultima_palabra, archivo_mezclado, lista):
    if len(lista) !=0:
        i=0
        while lista[i] == ultima_palabra:
            i+=1
        else:
            archivo_mezclado += lista[i] + " "
            ultima_palabra = lista[i]
            lista.pop(i)
             
    return ultima_palabra, archivo_mezclado, lista
                          
def principal(archivo1, archivo2):
    lista1 = sacar_palabras(archivo1)
    lista2 = sacar_palabras(archivo2)
    archivo_mezclado =""
    verificar = False
    ultima_palabra = "" 
    while (len(lista1)!= 0) or (len(lista2)!=0):
          if verificar == False:
              ultima_palabra, archivo_mezclado, lista1 = mezcla(ultima_palabra, archivo_mezclado, lista1)
              verificar = True
          else:
              ultima_palabra, archivo_mezclado, lista2 = mezcla(ultima_palabra, archivo_mezclado, lista2)
              verificar = False

    archivo_nuevo = open("resultado1.txt", "x")
    archivo_nuevo.write(archivo_mezclado)
    archivo_nuevo.close()
                      

principal("palabras1.txt", "palabras2.txt")
fin = time.time()
print(fin-inicio)
