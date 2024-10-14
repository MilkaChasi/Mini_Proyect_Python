import requests
import json

#Url
url = 'https://jsonplaceholder.typicode.com/comments'


#Obtener los datos
def obtener_datos(pagina=1, limite=10):
    
    params = {
        '_page': pagina,
        '_limit': limite
    }
     
    try: 
      respuesta = requests.get(url, params = params, timeout=5)
      if respuesta.status_code == 200: 
            product = json.loads(respuesta.content)  
            print(type(product))

    #Ordenar la columna postId de forma ascendente
            productos_ordenados = sorted(product, key=lambda x: int(x['postId']))
    #Imprimir encabezados
            print(f" {'ID_Usuario':<10} {'ID':<8} {'Nombre':<30} {'Email':<30} {'Comentario':<10}")  # Encabezados alineados
    # Imprimir los productos ordenados en su respectiva columna
            for producto in productos_ordenados:
                print(f"{producto['postId']:<12} {producto['id']:<5} {producto['name']:<25} {producto['email']:<20} {producto['body']:<10}")   
       
        # Guardar en archivo JSON
            guardar_en_json(product)
            print(f"Datos obtenidos exitosamente para la página {pagina}.")

    except requests.ConnectionError:
        print('Error: No se pudo conectar al servidor.')
    except requests.Timeout:
        print('Error: La solicitud ha superado el tiempo.')
    except requests.HTTPError as e:
        print(f'Error HTTP: {e.response.status_code} - {e.response.reason}')
    except json.JSONDecodeError:
        print('Error: No se pudo decodificar la respuesta JSON.')
    except Exception as e:
        print(f'Error inesperado: {e}')
        
        
# Guardar datos en un archivo JSON
def guardar_en_json(data):
    with open('datacomentarios.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print("Datos guardados en datacomentarios.json")

# Obtener datos de la página # con un límite de 10 
obtener_datos(pagina=1, limite=10)        



#Guardar los datos

def guardar_dato(id, nombre, email, comentario):
    parametros = { 'id': id, 'name': nombre, 'email':email, 'body': comentario }
    try:
        peticion = requests.post(url, json=parametros, timeout=5)
        peticion.raise_for_status() 
        respuesta = peticion.json()
        print(respuesta, 'Dato guardado')

    except requests.ConnectionError:
        print('Error: No se pudo conectar al servidor.')
    except requests.Timeout:
        print('Error: La solicitud ha superado el tiempo.')
    except requests.HTTPError as e:
        print(f'Error HTTP: {e.response.status_code} - {e.response.reason}')
    except json.JSONDecodeError:
        print('Error: No se pudo decodificar la respuesta JSON.')
    except Exception as e:
        print(f'Error inesperado: {e}')
#guardar_dato(501, 'katy Lopez', 'katylop@hotmail.com', 'cometario de ejemplo para prueba1')



#Actualizar los datos
def actualizar_dato(id, nombre, email, comentario):
    parametros = { 'id': id, 'name': nombre, 'email':email, 'body': comentario }
    try:
        peticion = requests.put(url + '/' + str(id), json=parametros, timeout=5)
        peticion.raise_for_status() 
        respuesta = peticion.json()
        print(respuesta, 'Dato actualizado')

    except requests.ConnectionError:
        print('Error: No se pudo conectar al servidor.')
    except requests.Timeout:
        print('Error: La solicitud ha superado el tiempo.')
    except requests.HTTPError as e:
        print(f'Error HTTP: {e.response.status_code} - {e.response.reason}')
    except json.JSONDecodeError:
        print('Error: No se pudo decodificar la respuesta JSON.')
    except Exception as e:
        print(f'Error inesperado: {e}')    
#actualizar_dato(1, 'Moni Smith', 'monismith@hotmail.com', 'cometario de ejemplo para prueba2')



#Eliminar los datos
def eliminar_dato(id):
    try:
        peticion = requests.delete(url + '/' + str(id), timeout=5)
        peticion.raise_for_status() 
        respuesta = peticion.json()
        print(respuesta, 'Dato eliminado')

    except requests.ConnectionError:
        print('Error: No se pudo conectar al servidor.')
    except requests.Timeout:
        print('Error: La solicitud ha superado el tiempo.')
    except requests.HTTPError as e:
        print(f'Error HTTP: {e.response.status_code} - {e.response.reason}')
    except json.JSONDecodeError:
        print('Error: No se pudo decodificar la respuesta JSON.')
    except Exception as e:
        print(f'Error inesperado: {e}')
#eliminar_dato(501)
