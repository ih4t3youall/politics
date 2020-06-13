import json
import requests
from objects import Ladron


api_url_base='http://www.senado.gov.ar/micrositios/DatosAbiertos/ExportarListadoSenadores/json'


response = requests.get(api_url_base)
if response.status_code == 200:
    jresponse = response.json()
    ladrones = jresponse['table']['rows']
    count = 0
    bloques = {}
    politicoBloque = {}
    for ladron in ladrones:
        count = count+1
        nombre = ladron['NOMBRE']
        apellido = ladron['APELLIDO']
        nombreCompleto = nombre+ ' ' + apellido
        bloque = ladron['BLOQUE']
        if bloque in bloques:
            bloques[bloque] = bloques[bloque] +1
            if bloque in politicoBloque:
                politicoBloque[bloque].append(nombreCompleto)
        else:
            bloques[bloque] = 1
            politicoBloque[bloque] = []
            politicoBloque[bloque].append(nombreCompleto)

    items = bloques.items();
    
    sumaTotal =0
    
    for item in items:
        print(item)
        sumaTotal = sumaTotal + item[1] 
    print(sumaTotal)
    if count == sumaTotal:
        print('las matematicas concuerdan')

        
    for i in politicoBloque:
        print(i)
        print(politicoBloque[i])
        print('-----------------------------------------')

    
