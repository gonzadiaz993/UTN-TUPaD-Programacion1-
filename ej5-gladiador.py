print("""
    =====BIENENIDO A LA ARENA DEL GLADIADOR=====
      """)
gladiador = input("Nombre del Gladiador:").title()
while not gladiador.isalpha() :
    gladiador = gladiador.isalpha()
    print("Error solo se permiten letras.")
    gladiador = input("Nombre del Gladiador:").title()
    

print(f"Bienvenido {gladiador}")

vida_del_Gladiador = 100
vida_del_Enemigo = 100
pociones_de_Vida = 3
daño_base_Ataque_Pesado = 15
Daño_base_del_enemigo = 12
Turno_Gladiador = True  

print(F"""
        ====INICIO DEL COMBATE====
---{gladiador} VIDA {vida_del_Gladiador}, ENEMIGO {vida_del_Enemigo}, pociones {pociones_de_Vida}---
ACCIONES DISONIBLES:
1)ATAQUE PESADO
2)RAFAGA VELOZ
3)CURAR 
""")
while vida_del_Enemigo > 0 and vida_del_Gladiador > 0 :
 print(F"""
        ====NUEVO TURNO====
---{gladiador} VIDA {vida_del_Gladiador}, ENEMIGO {vida_del_Enemigo}, pociones {pociones_de_Vida}---
ACCIONES DISONIBLES:
1)ATAQUE PESADO
2)RAFAGA VELOZ
3)CURAR 
""")
 opcion=input("EliGE ACCION(1,2,3): ")
 while not opcion.isdigit() or int(opcion) not in (1,2,3) :
   print("Ingresa solo numeros, y que esten dentro de la opciones(1,2.3).")
   opcion=input("EliGE ACCION(1,2,3): ")
 if opcion == "1":
   if vida_del_Enemigo < 20 :
      daño = (15 * 1.5)
      vida_del_Enemigo -= daño
      vida_del_Gladiador -= 12
      
      print(f"¡Atacaste al enemigo por {daño} puntos de daño!")
      print(f"el enemigo contraataca con {Daño_base_del_enemigo} de daño.")
   else:
      vida_del_Enemigo -= 20
      vida_del_Gladiador -= 12
      print(f"¡Atacaste al enemigo por {daño_base_Ataque_Pesado} puntos de daño!")
      print(f"el enemigo contraataca con {Daño_base_del_enemigo} de daño.")
 elif opcion == "2":
    for i in range(3):
       vida_del_Enemigo -=5
       print("Golpe conectado por 5 de daño.")
    vida_del_Gladiador -= 12
    print(f"el enemigo contraataca con {Daño_base_del_enemigo} de daño.")
 elif opcion =="3":
    if pociones_de_Vida > 0  :
       pociones_de_Vida -= 1
       vida_del_Gladiador += 30
    else:
       print("¡No quedan pociones!")
       print(f"el enemigo contraataca con {Daño_base_del_enemigo} de daño.")
if vida_del_Gladiador > 0 :
   print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
   print("---{gladiador} VIDA {vida_del_Gladiador}, ENEMIGO {vida_del_Enemigo}, pociones {pociones_de_Vida}---")
elif vida_del_Gladiador <= 0 :
    print("DERROTA. Has caído en combate.")
    print("---{gladiador} VIDA {vida_del_Gladiador}, ENEMIGO {vida_del_Enemigo}, pociones {pociones_de_Vida}---")
   
    
 