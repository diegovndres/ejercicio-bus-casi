import os 
import time
datos_cliente = []
ventas = []
bus = [["O" for x in range(4)] for y in range (5)]
ticket = 1500
while True:
    print("BIENVENIDO AL BUS TURBOMAN")
    print("1. Mostrar asientos disponibles")
    print("2. Comprar asiento")
    print("3. Mostrar ventas realizadas")
    print("4. Generar archivo de ventas")
    print("5. Salir")
    opc = int(input("Ingrese opcion: "))

    os.system('cls')
    if opc==1:
        for f in bus:
            print(f)
    elif opc==2:
        print("Comprar asiento :)")
        fila = int(input("Escoge fila(1-4): "))
        columna = int(input("Escoge columna(1-5): "))
        if bus[fila-1][columna-1] == 'O':
            bus[fila-1][columna-1] = 'X'
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        if edad < 18:
            ticket = ticket-(ticket*0.2)
            print(f"FELICIDADES TIENES UN DESCUENTO DEL 20%, SU PRECIO FINAL ES DE : {ticket}")
        elif edad > 65:
            ticket = ticket-(ticket*0.15)
            print(f"FELICIDADES TIENES UN DESCUENTO DEL 15%, SU PRECIO FINAL ES: {ticket} ")
        n_tel = int(input("Ingrese su numero de telefono: "))
        print(f"Reserva del asiento {fila,columna} realizada con exito")
        datos = [nombre,edad,n_tel,fila,columna]
        ventas.append(datos)

    elif opc==3:
        for x in ventas:
            print(x[0],x[1],
                  x[2],x[3],
                      x[4])
    elif opc==4:
        pass
    else:
        break
    
