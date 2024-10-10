#PRUEBA

import requests 
import json

url = 'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Ordinary_Drink'


def mostrar():
    peticion = requests.get(url)
    product = json.loads(peticion.content)
    
      
    if "drinks" in product:
        productos = product["drinks"]
        
        productos_ordenados = sorted(productos, key=lambda x: int(x['idDrink']))


        print("{:3} {:7} {:40} {:100} ".format(' ', 'ID_Bebida', 'Nombre_Bebida', 'Imagen'))
        num = 0
        
        for producto in productos_ordenados:
            num += 1
            print("{:3} {:7} {:40} {:100}".format(int(num), producto['idDrink'], producto['strDrink'], producto['strDrinkThumb']))
                 
#mostrar()



def guardar(id, nombre, imagen):
    parametros = { 'idDrink': id, 'strDrink': nombre, 'strDrinkThumb': imagen }
    peticion = requests.post(url, parametros)
    respuesta = json.loads(peticion.content)


#guardar('17841', 'Margarita', 'https://www.recetasderechupete.com/wp-content/uploads/2024/03/coctel_margarita_marie_brizard-1200x828.jpg')



def actualizar(id, nombre, imagen):
    parametros = { 'idDrink': id, 'strDrink': nombre, 'strDrinkThumb': imagen }
    peticion = requests.put(url + '/' + id ,parametros)
    respuesta = json.loads(peticion.content)


def eliminar(id):
    peticion = requests.delete(url + '/' + id)
    respuesta = json.loads(peticion.content)


def procesar(respuesta, mensaje):
    status = respuesta[0]['status']
    if status == 'error':
        claves = []
        errores = respuesta[1]['errors']
        for err in errores:
            claves.append(err)
        for c in claves:
            print(errores[c][0])
                


    else:
        print(mensaje)


mostrar()