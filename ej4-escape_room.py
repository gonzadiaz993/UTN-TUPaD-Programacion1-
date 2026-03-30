energia = 100
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
contador_forzar = 0

print("ESCAPE ROOM: LA BOVEDA")
while True:
 nombre_agente =input("ingrese su nombre:")
 if nombre_agente.isalpha():
  nombre= nombre_agente
  nombre = nombre.title()
  
  print(f"Bienvenido agente {nombre} ")
  break
 else:
    print("Ingrese solo letras.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <=3):
    print(""" 
        MENU PRINCIPAL
        1)Forzar cerradura.(costo: -20 energía, -2 tiempo)
        2)Hackear panel. (costo: -10 energía, -3 tiempo) 
        3)Descarnsa.(costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra) 
""")
    print(f"energia = {energia}, tiempo = {tiempo}, cerraduras abiertas = {cerraduras_abiertas}, alarma= {alarma}")
    menu =input("ingrese la opcion deseada:")
    while not menu.isdigit() or menu not in ["1", "2", "3"]:
        menu = input("Opción inválida. Ingrese 1, 2 o 3: ")

    if menu == "1":
      contador_forzar +=1
      energia -= 20
      tiempo -= 2
      if contador_forzar == 3 :
         alarma = True
         print("La cerradura se trabó, alarma activada por forzar demasiado.")
         print(f"energia = {energia}, tiempo = {tiempo}, cerraduras abiertas = {cerraduras_abiertas}")
         cerraduras_abiertas -=1
      else:
          if energia < 40 :
                print("¡¡riesgo de alarma!!")
                numero_a=input("ingrese un numero del 1 al 3:")
                while not numero_a.isdigit() or (numero_a != "1" and numero_a != "2" and numero_a !="3"):
                 numero_a = input("Numero invalido, elije un muero entre el 1 y el 3: ")
                if numero_a =="3":
                   alarma = True
                   print("activaste la alarma.")
                   print(f"energia = {energia}, tiempo = {tiempo}, cerraduras abiertas = {cerraduras_abiertas}")
                
                   
          if alarma == False :
              cerraduras_abiertas +=1
              print("¡¡lograste abrir una cerradura!!")
              print(f"energia = {energia}, tiempo = {tiempo}, cerraduras abiertas = {cerraduras_abiertas}")
    elif menu == "2": 
         contador_forzar = 0
         energia -=10
         tiempo -=3
         print("iniciando hackeo.")
         for i in range(4):
            codigo_parcial += "A"
            print(f"el progreso del codigo: {codigo_parcial}")
         if len(codigo_parcial) >= 8:
             if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡sistema hackeado! una cerradura abierta.")
    elif menu == "3":
       contador_forzar= 0
       energia += 15
       tiempo -= 1
       if energia > 100 :
          energia=100
       if alarma :
          energia -=10 
if cerraduras_abiertas == 3:
   print(f"agente {nombre} lograste abrir todas las cerraduras. ")
elif energia <= 0 or tiempo <= 0 :
   print(f"agente {nombre} tu mision fracaso.")
else:
   alarma = True
   print("sistema bloqueado. La alarma te delato.")


        

