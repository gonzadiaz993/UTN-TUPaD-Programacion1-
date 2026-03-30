usuario_correcto= "a"
contraseña_correcta = "a1"
intentos=3
acceso = False
opcion=""

while intentos > 0:
    usuario=input("ingrese usuario:")
    contraseña=(input("ingrese contraseña:"))
    if usuario == usuario_correcto and contraseña == contraseña_correcta:
        acceso=True
        print("acceso correcto.")
        break
    else:
        intentos -=1
        if intentos >0:
            print(f"Te quedan {intentos}")
        else:
            print("te quedaste sin intentos.")
            print("cuata bloqueada.")
if acceso:
    while opcion != 4:
        print("""
                ----menu seguro---
          1. Ver estado de inscripción.
          2. Cambiar clave.
          3. Mostrar mensaje motivacional
          4. Salir.
           """)
        while True:
            opcion=input("ingrese una opcion del menu: ")
            if opcion.isdigit():
               opcion= int(opcion)
               if 1<= opcion <=4:
                    break
               else:
                  print("opcion fuera de rango")
            else:
                print("debe ingresar un numero.")      
           
        match opcion :
                case 1 :
                    print("usted esta inscripto en el cursado.")
                case 2 :
                     while True:
                        clave_nueva = input("Ingrese nueva clave(La nueva clave debe tener mínimo 6 caracteres): ")
                        confirmacion_clave= input("Ingrese nuevamente la clave: ")
                        if len(clave_nueva) >= 6:
                            if clave_nueva == confirmacion_clave:
                                print("cambio exitoso.")
                                break
                            else:
                                print("fallo en el cambio de clave.")
              
                case 3:
                    print("El éxito es la suma de pequeños esfuerzos repetidos día tras día; cada página que lees hoy es un escalón más hacia la meta que mañana alcanzarás.")
                case 4:
                     print("cerrando secion.")
                case "":
                    print("opcion invalida.")
 