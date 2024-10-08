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
        
