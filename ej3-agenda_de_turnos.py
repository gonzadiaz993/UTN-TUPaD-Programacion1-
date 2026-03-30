print("Bienvenido a Mr.Turnos")
nombre=input("ingrese su nombre:")
opcion=""
dia_lunes= 1
dia_martes= 2
lunes1 ="libre"
lunes2="libre"
lunes3="libre"
lunes4="libre"
martes1="libre"
martes2="libre"
martes3="libre"

while opcion != "5":
    print("""
            1. Reservar turno 
            2. Cancelar turno (por nombre) 
            3. Ver agenda del día 
            4. Ver resumen general 
            5. Cerrar sistema
           """)
    opcion=input(f"{nombre} ingrese la opcion deseada: ")
    match opcion:
         case "1":
              #reservar dia
              nombre_paciente = input("ingrese su nombre: ")
              if nombre_paciente.isalpha() :
                    nombre_paciente1=nombre_paciente
              

              
                    dia= input("""
                                 -1) si desea el turno para el lunes
                                 -2) si desea el turno para el dia martes 
                                 """)
                    if dia.isdigit():
                      dia1 = dia
                     
                      match dia1 :
                       case "1" :
                            if nombre_paciente1 in (lunes1, lunes2, lunes3, lunes4):
                              print("paciete ya tiene turno")
                            elif lunes1 == "libre":
                                 lunes1 = nombre_paciente1
                                 print("turno agregado con exito.")
                            elif lunes2 == "libre": 
                             lunes2 = nombre_paciente1
                             print("turno agregado con exito.")
                            elif lunes3 == "libre": 
                             lunes3 = nombre_paciente1
                             print("turno agregado con exito.")
                            elif lunes4 == "libre": 
                             lunes4 = nombre_paciente1
                             print("turno agregado con exito.")
                            else:
                             print("lunes sin turnos.")
                       case "2":
                          if nombre_paciente1 in (martes1, martes2):
                               print("el paciente ya tiene turno.")
                          elif martes1== "libre" :
                               martes1 = nombre_paciente1
                               print("turno agregado con exito.")
                          elif martes2 == "libre":
                               martes2 = nombre_paciente1
                               print("turno agregado con exito.")
                          elif martes3 == "libre":
                               martes3 = nombre_paciente1
                               print("turno agregado con exito.")
                               
                          else:
                               print("martes sin turno.")
                       case _:
                          print("opcion invalida.")
                    else:
                     print("ingreso incorrecto.")    
              else:
                  print("debe solo letras.")         
               
         case "2":
              dia= input("ingrese el dia del turno 1) lunes 2) martes : ")
              paciente_eliminar = input("ingrese nombre del paciente: ")
              if paciente_eliminar.isalpha():
                   paciente_borrar =paciente_eliminar
              else:
                   print("ingrese un nombre correcto")
              if dia.isdigit():
                  dia1 = dia    
                  match dia1:
                    case "1":
                        if lunes1 == paciente_borrar:
                             lunes1 = "libre"
                             print("turno eliminado con exito.")
                        elif lunes2 == paciente_borrar:
                             lunes2 = "libre"
                             print("turno eliminado con exito.")
                        elif lunes3 == paciente_borrar:
                             lunes3 = "libre"
                             print("turno eliminado con exito.")
                        elif lunes4 == paciente_borrar:
                             lunes4 = "libre"
                             print("turno eliminado con exito.")
                        else:
                             print(f"El paciente {paciente_borrar} no tiene turno el dia lunes")
                    case "2":
                        if martes1 == paciente_borrar:
                           martes1 = "libre"
                           print("turno eliminado con exito.")
                        elif martes2 == paciente_borrar:
                             martes2 = "libre"
                             print("turno eliminado con exito.")
                        elif martes3 == paciente_borrar:
                             martes3 = "libre"
                             print("turno eliminado con exito.")
                        else:
                             print(f"El paciente {paciente_borrar} no tiene turno el dia martes.")
                    case "":
                        print("opcion invalida")         
              else:
                        print("ingreso incorrecto.")         
         case"3":
              dia_consulta=input("""
                              Elige el dia a consultar turnos.
                                                            -1) lunes.
                                                            -2) martes. 
                                  """)
              if dia_consulta.isdigit():
                   dia_consulta1=dia_consulta                  
                   match dia_consulta1:
                     case "1":
                         print(f"""
                    -turnos del dia lunes:
                                         -lunes 1: {lunes1}
                                         -lunes 2: {lunes2}
                                         -lunes 3: {lunes3}
                                         -lunes 4: {lunes4}""")
                     case "2":

                      print(f"""-turnos del dia martes:
                                         -martes 1: {martes1}
                                         -martes 2: {martes2}
                                         -martes 3: {martes3}""")
                     case _:
                        print("opcion invalida") 
              else:
                   print("debe ingresar un numero.") 
              
         case "4":
              dia_ocupadosL= 0
              dia_ocupadosM= 0
              
              
              if lunes1 != "libre":
                             dia_ocupadosL +=1
              if lunes2 != "libre":
                             dia_ocupadosL +=1
              if lunes3 != "libre":
                             dia_ocupadosL +=1
              if lunes4 != "libre":
                             dia_ocupadosL +=1
              
              if martes1 != "libre":
                             dia_ocupadosM +=1       
              if martes2 != "libre":
                             dia_ocupadosM +=1
              if martes3 != "libre":
                             dia_ocupadosM +=1
              
              elegir_dia= input("""
                                ingrese el dia para ver la agenda de turnos 
                                -1) lunes
                                -2) martes 
                                -3)para ver el dia con mas turnos. 
                                """)
              if elegir_dia.isdigit():
                   dia_aelegir=elegir_dia
              
                   match dia_aelegir:
                         case "1":
                               print(f"""
                                   -turnos del dia lunes:
                                                        -lunes 1: {lunes1}
                                                        -lunes 2: {lunes2}
                                                        -lunes 3: {lunes3}
                                                        -lunes 4: {lunes4}
                    """)
                               print(f"cantidad de dias ocupados {dia_ocupadosL}")
                         case "2":
                               print(f"""
                               turnos del dia martes:
                                                    -martes 1: {martes1}
                                                    -martes 2: {martes2}
                                                    -martes 3: {martes3}
                    """)
                               print(f"cantidad de dias ocpuados {dia_ocupadosM}")
                         case "3":
                               
                          if dia_ocupadosL > dia_ocupadosM:
                             print("el lunes es el dia con mas turnos.")
                          elif dia_ocupadosM > dia_ocupadosL :
                             print("el martes es el dia con mas turnos.")
                          else:                               
                             print("tanto lunes como martes tienen la misma cantidad de turnos ocupados.")
              else:
                   print("debe elegir un numero.")
                                  

         case "5":
              print("¡¡¡Hasta luego, gracias por usar Mr: Turnos!!!")