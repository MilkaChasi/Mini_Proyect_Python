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
    respuesta = peticion.json()
   
    print(respuesta,'Producto guardado')


#guardar(17841, 'Margarita', 'https://www.recetasderechupete.com/wp-content/uploads/2024/03/coctel_margarita_marie_brizard-1200x828.jpg')



def actualizar(id, nombre, imagen):
    parametros = { 'idDrink': id, 'strDrink': nombre, 'strDrinkThumb': imagen }
    peticion = requests.put(url + '/' + str(id), json=parametros)
    respuesta = peticion.json()
   
    print(respuesta,'Producto actualizado')

#actualizar(15300, 'Gone', 'https://www.thecocktaildb.com/images/media/drink/xtuyqv1472669026.jpg')


def eliminar(id):
    peticion = requests.delete(url + '/' + str(id))
    respuesta = peticion.json()
   
    print(respuesta,'Producto eliminado')

#eliminar(17841)