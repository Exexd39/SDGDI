"""
Cambiar las listas por diccionario [X]
Cambiar las funciones para que usen diccionarios [X]
Busqueda de diccionarios dentro de listas [X]
Agregar el procesamiento de codigos de productos []
"""
opcion=0

lista_productos = []
"""
producto = {
    "Nombre" : nombre,
    "Cantidad" : stock,
    "Precio" : precio
}
"""

def solicitarProducto():
    nombreProd= input("Ingrese el nombre del nuevo producto: ").capitalize()
    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
            return [nombreProd,precioProd,stockProd]
            
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):

    for producto in lista_productos:
        if producto["Nombre"].capitalize() == nombre.capitalize():
            return producto

    #return None  #Si no pasa el if por automatico retorna none por defecto.
        
def guardarProducto(nombre,precio,stock):
    
    if buscarProducto(nombre) == None:
        producto = {"Nombre" : nombre,"Cantidad" : stock,"Precio" : precio}  #Igual a diccionario solo que hacia el lado. 
        lista_productos.append(producto)
        print("Producto Guardado")
    else:
        print("Ya existe un producto con ese nombre.")
       

def actualizarProducto(nombre,Nuevostock,Nuevoprecio):
    productoBuscado = buscarProducto(nombre)
    if productoBuscado != None:
        indice = lista_productos.index(productoBuscado)
        productoBuscado["Cantidad"] = Nuevostock
        productoBuscado["Precio"] = Nuevoprecio
        #actualizar el producto en la lista de productos
        lista_productos[indice] = productoBuscado
        print(f"El producto {nombre} fue actualizado correctamente.")
    else:
        print("El producto que intenta actualizar no existe.")

def mostrarInventario():
    if len(lista_productos) == 0:
        print("No hay ningun producto aun.")
    else:
        for a in lista_productos:
            print(f"Nombre: {a["Nombre"]} \t\t Precio: ${a["Cantidad"]} \t\t Stock: {a["Precio"]}")
                
def eliminarProducto(nombre_producto): 
    if productoBuscado != None:
        productoBuscado = buscarProducto(nombre_producto)
        lista_productos.remove(productoBuscado)
        print("Producto Eliminado.")
    else:
        print("No existe ningun producto con ese nombre.")

while opcion!= "6":
    print("**************Menu de gestión de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opción que desea(1-6): ")

    match opcion:
        case "1":
            infoProducto = solicitarProducto()
            if infoProducto != None:
                guardarProducto(infoProducto[0],infoProducto[1],infoProducto[2])

        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ").capitalize()
            productoEncontrado=buscarProducto(nombre) #Usa el valor que ingresamos
            if productoEncontrado!=None:  #Si tiene algo entonces hacer:
                print("-" * 60)
                print(f"Nombre: {productoEncontrado["Nombre"]} \t\t Precio: ${productoEncontrado["Cantidad"]} \t\t Stock: {productoEncontrado["Precio"]}")
                print("-" * 60)
        case "3":
            infoProducto = solicitarProducto()
            if infoProducto != None:
                actualizarProducto(infoProducto[0], infoProducto[2], infoProducto[1])
        case "4":
            print("-" * 60)
            mostrarInventario()
            print("-" * 60)
        case "5":
            nombre=input("Ingrese el nombre del producto a eliminar: ").capitalize()
            eliminarProducto(nombre)
        case "6":
            print("Saliendo del programa...")
        case default:
            print("Opcion no valida.")