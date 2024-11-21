from conexion import conectar

# Esta función sirve para registrar un cliente nuevo en la base de datos.
def registrar_cliente():
    # Primero conectamos con la base de datos.
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Pedimos los datos necesarios al usuario.
            nombre = input("Nombre del cliente: ")
            apellido = input("Apellido del cliente: ")
            correo = input("Correo electrónico: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección: ")

            # Hacemos una consulta para añadir los datos a la tabla 'Clientes'.
            query = """
            INSERT INTO Clientes (nombre, apellido, correo, telefono, direccion)
            VALUES (%s, %s, %s, %s, %s)
            """
            valores = (nombre, apellido, correo, telefono, direccion)
            
            # Ejecutamos la consulta y guardamos los cambios en la base de datos.
            cursor.execute(query, valores)
            conexion.commit()
            print("Cliente registrado con éxito.")
        except Exception as e:
            print(f"Error al registrar el cliente: {e}")
        finally:
            # Cerramos el cursor y la conexión con la base de datos.
            cursor.close()
            conexion.close()

# Esta función sirve para mostrar todos los clientes registrados en la base de datos.
def listar_clientes():
    # Conectamos con la base de datos.
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Hacemos una consulta para obtener todos los datos de los clientes.
            query = "SELECT * FROM Clientes"
            cursor.execute(query)
            
            # Mostramos los datos obtenidos.
            clientes = cursor.fetchall()
            print("Clientes registrados:")
            for cliente in clientes:
                print(cliente)
        except Exception as e:
            # Mostramos un mensaje si hay algún error al listar los clientes.
            print(f"Error al listar los clientes: {e}")
        finally:
            # Cerramos el cursor y la conexión.
            cursor.close()
            conexion.close()

# Esta función sirve para buscar a un cliente por su correo electrónico.
def buscar_cliente_por_correo():
    # Conectamos con la base de datos.
    conexion = conectar()
    if conexion:
        try:
            cursor = conexion.cursor()
            
            # Pedimos al usuario el correo del cliente que quiere buscar.
            correo = input("Introduce el correo del cliente: ")
            
            # Hacemos una consulta para buscar al cliente por su correo.
            query = "SELECT * FROM Clientes WHERE correo = %s"
            cursor.execute(query, (correo,))
            
            # Si encontramos al cliente, mostramos sus datos.
            cliente = cursor.fetchone()
            if cliente:
                print("Datos del cliente:", cliente)
            else:
                # Si no existe, mostramos un mensaje indicando que no se encontró.
                print("Cliente no encontrado.")
        except Exception as e:
            # Mostramos un mensaje si hay un error en la búsqueda.
            print(f"Error al buscar el cliente: {e}")
        finally:
            # Cerramos el cursor y la conexión.
            cursor.close()
            conexion.close()
