from clientes import registrar_cliente, listar_clientes, buscar_cliente_por_correo  # Importo funciones de clientes
from pedidos import realizar_compra, seguimiento_compra  # Importo funciones de pedidos

def menu():
    while True:
        print("\nMenu de gestion de pedidos: ")
        print("1. Registrar Cliente")
        print("2. Ver Clientes")
        print("3. Buscar Cliente por Correo")
        print("4. Realizar Compra")
        print("5. Seguimiento de Compra")
        print("0. Salir")
        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            registrar_cliente()  # Registrar cliente
        elif opcion == "2":
            listar_clientes()  # Listar clientes
        elif opcion == "3":
            buscar_cliente_por_correo()  # Buscar cliente por correo
        elif opcion == "4":
            realizar_compra()  # Realizar una compra
        elif opcion == "5":
            seguimiento_compra()  # Hacer seguimiento de compra
        elif opcion == "0":
            print("Ha salido del programa.")
            break  # Salir del bucle
        else:
            print("Opcion no valida. Intentalo de nuevo.")
