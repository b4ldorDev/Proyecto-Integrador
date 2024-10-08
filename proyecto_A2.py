def requerimiento_2a(datos):
    encabezado=datos[0]
    registros=len(datos)-1
    campos=len(encabezado)
    print(f"Número de campos(columna): {campos}")
    print(f"Número de registros(fila): {registros}")
    i=0
    while i<campos:
        columna=encabezado[i]
        datcol=[fila[i] for fila in datos[1:]]
        numero=True
        for val in datcol:
            if val.isdigit()==True:
                numero=True
            else:
                numero=False
        letra=True
        for val in datcol:
            if val.isalpha()==True:
                letra=True
            else:
                letra=False
        alphanum=True
        for val in datcol:
            if val.isalnum()==True:
                alphanum=True
            else:
                alphanum=False
        especiales=True
        for val in datcol:
            if val.isalnum()==False:
                especiales=True
            else:
                especiales=False
        vacios=0
        for val in datcol:
            if val==" ":
                vacios+=1
        procentaje=(vacios/registros)*100
        print(f"Columna: {columna}")
        print(f"Numéricos: {numero}")
        print(f"Alfabéticos: {letra}")
        print(f"Alfanuméricos: {alphanum}")
        print(f"Especiales: {especiales}")
        print(f"Porcentaje de datos vacios: ",procentaje"%")
