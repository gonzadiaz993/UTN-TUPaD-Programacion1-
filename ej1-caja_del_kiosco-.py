nombre=input("Ingrese nombre del cliente: ").strip()

while not nombre.isalpha():
        print("Ingrese solo letras")
        nombre=input("Ingrese nombre del cliente: ")


productos=input("Ingrese la cantidad de productos a comprar: ")

while not productos.isdigit():
        print("ingrese solo numeros.")
        productos=input("Ingrese la cantidad de productos a comprar:")
        while productos == "0":
               productos=input("Ingrese la cantidad de productos a comprar:")
               
productos=int(productos)
print(f"Ingreso {productos}")

cont=0
s = str("s")
n= str("n")
descuento_10 = 0
precio_final = 0
ahorro = 0
total = 0

for i in range(productos):
    cont += 1
    precio=float(input(f"precio del producto {cont}: "))
    descuento=input("¿TIene descuento? (s/n): ").lower()
    while descuento != "s" and descuento != "n":
           print("ingrese solo |s| o |n|.  ")
           descuento=input("¿TIene descuento? (s/n): ").lower()

    if descuento == s:
           total += precio
           descuento_10 = precio * 0.10
           ahorro += descuento_10
           precio_final= precio * 0.90
           
           
           print(f"producto {cont} -- precio: {precio_final} descuento si.")
    else:
           total += precio
           
           print(f"producto {cont} -- precio: {precio}--descuento no.")
total_cdescuento = total - ahorro
promedio = total / cont
print(f"cliente: {nombre}")
print(f"precio total sin descuento: {total}")
print(f"precio total con descuento: {total_cdescuento}")
print(f"ahorro total: {ahorro}")
print(f"promedio de precio por producto: {promedio:.2f}")