 #Tienda virtual 

cantidad_pedidos = int(input("¿Cuántos pedidos se van a ingresar? "))

# Lista para almacenar los pedidos

pedidos = []

# Datos requeridos para el usuario 

for i in range(cantidad_pedidos):
    print("Pedido número:", i)
    nombre = input("Nombre del cliente: ")
    valor = float(input("Valor total del pedido: "))
    estado = input("Estado del pedido (pendiente, enviado o cancelado): ")
    pendiente = estado == "pendiente"
    enviado = estado == "enviado"
    cancelado = estado == "cancelado"

    if pendiente or enviado or cancelado:
        estadoF = estado
    else:
        print("Estado inválido. Se marcará como 'cancelado'.")
        estadoF = "cancelado"

    pedido = {
        "nombre": nombre,
        "valor": valor,
        "estado": estadoF
    }
    
    #Estadistica 

    total_procesados = len(pedidos)
    total_enviados = 0
    monto_total = 0
    pendientes = 0
    pedido_mayor = pedidos[0]

    print("Estas son las stadísticas")
    print("Total de pedidos procesados:", total_procesados)
    print("Total de pedidos enviados:", total_enviados)
    print("Monto total en ventas: $", monto_total)
    print("Cliente con el pedido de mayor valor:", pedido_mayor["nombre"], "(", pedido_mayor ["valor"], ")")
    porcentajeP = (pendientes / total_procesados) * 100
    if porcentajeP > 70:
        print("¡ALERTA MUCHOS PEDIDOS SIN PROCESAR!")