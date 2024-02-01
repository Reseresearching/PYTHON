

# COMO una persona normal
# QUIERO convertir F a C
# PARA SABER a que temperatura estan en USA
"""
celsius = int(input("cuantos grados hace?"))

resultado=(celsius*9/5)+32
print(str(resultado))

x=()tuple
x=[]list
x=
"""
"""
for numero in range(101):
    print(f"numero {numero}")


 
#Crear una tupla con números del 0 al 100 usando range()
tupla_numeros = tuple(range(101))
# Imprimir la tupla
print(tupla_numeros)

   """

"""
x=(3,5,"hola")

for i in x:
    print(i)

"""
"""
x=set(4, 6, 8, "hola")
print(type(x))
print(x)
x[2]="agur"

"""
x=45.674
y=int(x)
print(y)


loggedIn = False
print (int(loggedIn))


a={10, 20, 30, 40}
b={30,40,50,60}
print(a.union(b))

a=set()

listaRespuestas=[10,20,"agur","AGUR",10,50]
setRespuestas=set(listaRespuestas)
print(setRespuestas)

x=43.7
print(int(x))
      
x=23.4567
print(f"{x:.2f}")


valores=range(100)
for x in valores:
    print(x)

s="Python es genial!"
print("python" in s)

s="PYTHON ES MI FAVORITO"
print(s[3])

listadealumnos=["jon", "maria"]


compra=["manzana","platanos","kiwi"]
print(compra[0])
print(len(compra))

compra.append("piña")
print(compra)
compra.remove("piña")
print(compra)

for i in compra:
     print("fruta es"+i)


for i in compra:
    if i== "platano":
        print("fruta es"+i)

    else:   
        print("no hay platano")
print("end")


compra=["manzana","platanos","kiwi"]
print(compra[0])
print(len(compra))

compra.append("piña")
print(compra)
compra.remove("piña")
print(compra)
compra.sort()
print(compra)

nuevalista=[i.capitalize for i in compra]













"""

class Tienda:
    def __init__(self):
        self.productos = {
            "manzanas": {"precio": 2.0, "especial": False},
            "zumos": {"precio": 3.0, "especial": True},
            "leche": {"precio": 1.5, "especial": False}
        }

    def mostrar_especiales(self):
        especiales = [producto for producto, info in self.productos.items() if info["especial"]]
        return especiales

    def mostrar_productos(self):
        for producto, info in self.productos.items():
            print(f"{producto}: {info['precio']} euros{' (especial)' if info['especial'] else ''}")

    def hacer_compra(self, dinero):
        print("Elija el producto que desea comprar:")
        self.mostrar_productos()
        seleccion = input()
        
        if seleccion in self.productos:
            precio = self.productos[seleccion]["precio"]
            if self.productos[seleccion]["especial"]:
                descuento = 0.1  # Descuento del 10% para productos especiales
                precio -= precio * descuento

            if dinero >= precio:
                cambio = dinero - precio
                print(f"¡Ha comprado {seleccion}! Su cambio es de {cambio} euros.")
            else:
                print("Dinero insuficiente. ¡Compra cancelada!")
        else:
            print("Producto no válido.")

# Uso de la aplicación

print("Bienvenidos a la tienda. Hoy tenemos especiales de:")
print(tienda.mostrar_especiales())

while True:
    print("\nIntroducir '1' para ver todos los productos, '2' para hacer una compra, '3' para salir.")
    opcion = input()

    if opcion == '1':
        tienda.mostrar_productos()
    elif opcion == '2':
        print("Introduzca la cantidad de dinero que tiene:")
        dinero = float(input())
        tienda.hacer_compra(dinero)
    elif opcion == '3':
        print("Gracias por visitar la tienda. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")


"""


print("Bienvenidos a mi tienda. Hoy tenemos especiales de:") #compra=["manzana","platanos","kiwi"]

print("         manzanas")
print("         zumos")
print("         leche")
print("         zanahorias")


inventario=["manzanas","zumos", "piñas", "leche", "zanahorias","platanos","kiwi", "mango"]


accion= int(input("Introducir 1 para ver todos los productos,'2' para hacer una compra…, '3' para borrar un producto,"))
lacompra =[]   #podia haber hecho esto :    lacompra =["Tiquet"]
#while not accion ==4:
if accion==1:
    print("         manzanas")
    print("         zumos")
    print("         leche")
    print("         zanahorias")  

    for i in inventario:
        print(f"fruta es {i}")  
    
elif accion==2:

    """
    print("AHORA ESTAS COMPRANDO ")
    lacompra=lacompra.append(str(input("Escribe el producto")))
    if lacompra in inventario:
        for _ in range(4):
            compraProducto= str(input("¿Qué quieres comprar?"))
            lacompra.append(compraProducto)
            print(lacompra)
        
    else:
        print("No esta en la lista")
    
    compraProducto2= str(input("¿Qué quieres comprar?"))
    lacompra.append(compraProducto2)
    print(lacompra)
    """
    pass
elif accion==3:




    
    
    print(compra[0])
    print(len(compra))

    compra.append("piña")
    print(compra)
    compra.remove("piña")
    print(compra)

    


    for i in compra:
        if i== "platano":
            print("fruta es"+i)

        else:   
            print("no hay platano")
    print("end")
    pass
else :
    print("gracias por tu compra")


""""
print(compra[0])
print(len(compra))

compra.append("piña")
print(compra)
compra.remove("piña")
print(compra)
compra.sort()
print(compra)

nuevalista=[i.capitalize for i in compra]

"""
