from conexion import conectar  # Importo la función para conectar a la base de datos

def realizar_compra():
    conexion = conectar()  # Establezco la conexión
    if conexion:
        try:
            cursor = conexion.cursor()
            id_cliente = int(input("ID del cliente que realiza la compra: "))

            # Verifico si el cliente existe en la base de datos
            query_cliente = "SELECT * FROM Clientes WHERE id_cliente = %s"
            cursor.execute(query_cliente, (id_cliente,))
            cliente = cursor.fetchone()
            if not cliente:
                print(f"Error: No existe un cliente con el ID {id_cliente}.")
                return

            # Creo un nuevo pedido para el cliente
            query_pedido = "INSERT INTO Pedidos (id_cliente) VALUES (%s)"
            cursor.execute(query_pedido, (id_cliente,))
            id_pedido = cursor.lastrowid
            print(f"Pedido creado con éxito. ID del pedido: {id_pedido}")

            while True:
                id_producto = int(input("ID del producto a añadir (0 para finalizar): "))
                if id_producto == 0:
                    break  # Salgo del bucle si se introduce 0
                cantidad = int(input("Cantidad del producto: "))

                # Obtengo los detalles del producto (precio y stock)
                query_producto = "SELECT precio, stock FROM Productos WHERE id_producto = %s"
                cursor.execute(query_producto, (id_producto,))
                producto = cursor.fetchone()
                if producto:
                    precio_unitario, stock_disponible = producto
                    if cantidad > stock_disponible:
                        print(f"Stock insuficiente. Solo hay {stock_disponible} unidades disponibles.")
                        continue  # Pido otro producto si el stock es insuficiente

                    # Registro el detalle del pedido
                    query_detalle = """
                    INSERT INTO DetallePedidos (id_pedido, id_producto, cantidad, precio_unitario)
                    VALUES (%s, %s, %s, %s)
                    """
                    valores = (id_pedido, id_producto, cantidad, precio_unitario)
                    cursor.execute(query_detalle, valores)

                    # Actualizo el stock del producto
                    query_actualizar_stock = "UPDATE Productos SET stock = stock - %s WHERE id_producto = %s"
                    cursor.execute(query_actualizar_stock, (cantidad, id_producto))

                    conexion.commit()  # Confirmo la transacción
                    print(f"Producto {id_producto} añadido al pedido.")
                else:
                    print("Producto no encontrado.")

        except Exception as e:
            print(f"Error al realizar la compra: {e}")
        finally:
            cursor.close()
            conexion.close()  # Cierro la conexión

def seguimiento_compra():
    conexion = conectar()  # Establezco la conexión
    if conexion:
        try:
            cursor = conexion.cursor()
            id_pedido = int(input("Introduce el ID del pedido: "))
            query = """
            SELECT p.id_pedido, c.nombre, c.apellido, pr.nombre_producto, d.cantidad, d.precio_unitario
            FROM Pedidos p
            INNER JOIN Clientes c ON p.id_cliente = c.id_cliente
            INNER JOIN DetallePedidos d ON p.id_pedido = d.id_pedido
            INNER JOIN Productos pr ON d.id_producto = pr.id_producto
            WHERE p.id_pedido = %s
            """
            cursor.execute(query, (id_pedido,))
            detalles = cursor.fetchall()
            if detalles:
                print("Detalles del pedido:")
                for detalle in detalles:
                    print(detalle)
            else:
                print("Pedido no encontrado.")
        except Exception as e:
            print(f"Error al realizar el seguimiento de la compra: {e}")
        finally:
            cursor.close()
            conexion.close()  # Cierro la conexión
