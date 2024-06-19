print ("Bienvenido al sistema de generaciones de tablas de multiplicar")
opcionMenu="4"
multiplicando=0
resultado=0
tabla=""
while opcionMenu!=3:
    print("1.- Generar la tabla")
    print("2.- Exportar la tabla")
    print("3.- salir")
    
    opcionMenu=input("> ")
    match opcionMenu:
        case "1":
            tabla=""
            while True:
                try:
                    multiplicando=int(input("ingrese el multiplicador"))
                except ValueError:
                    print("solo puede ingresar valores numericos")
                else:
                    break
            for i in range(1,11):
                resultado=i*multiplicando
                tabla+=f"{multiplicando} X {i} = {resultado}\n"
            print(tabla)
        case "2":
            if tabla!="":
                with open ("tabla.txt", "w") as archivo:
                    archivo.write(tabla)
                    print("archivo guardado exitosamente")
            else:
                print("""primero debe generar los datos de la tabla.
                      para eso seleccione la opcion 1 del menu""")