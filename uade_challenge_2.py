import time
def contar_pases_y_efectividad(archivo_de_pases):
    with open(archivo_de_pases, "r") as archivo:
        lista = []
        diccionario_auxiliar={}
        lineas = archivo.readlines()
        for linea in lineas:
            datos = linea.split(';')
            if datos[2] in diccionario_auxiliar:
                diccionario_auxiliar[datos[2]] = [diccionario_auxiliar[datos[2]][0] + int(datos[3]), diccionario_auxiliar[datos[2]][1] + 1, datos[0],datos[1]]
            else:
                diccionario_auxiliar[datos[2]] = [int(datos[3]), 1, datos[0],datos[1]]
        for i in diccionario_auxiliar:
            diccionario_auxiliar[i].append(round((diccionario_auxiliar[i][0]/diccionario_auxiliar[i][1])*100, 2))
        diccionario_auxiliar = dict(sorted(diccionario_auxiliar.items(), key=lambda item: item[1][4], reverse=True))

        for jugadoras, jugadas in diccionario_auxiliar.items():
            pais_existete = False
            if len(lista)>0:
                for i in range(len(lista)):
                    if jugadas[2] in lista[i]:
                        pais = i
                        pais_existete = True
                if pais_existete == False:
                    lista.append({jugadas[2]:[]})
                    pais = len(lista)-1
            else:
                lista.append({jugadas[2]:[]})
                pais = len(lista)-1

            info_jugadora = {"Numero": jugadas[3], "Nombre": jugadoras, "Cantidad_pases": jugadas[1], "pases_bien" : jugadas[0], "pases_mal": int(jugadas[1])- int(jugadas[0]), "porcentaje": jugadas[4]}
            lista[pais][jugadas[2]].append(info_jugadora)
        
    return lista

lista = contar_pases_y_efectividad("jugadas.txt")

