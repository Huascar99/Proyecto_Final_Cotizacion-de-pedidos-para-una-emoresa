import validaciones
import calculos
import interfaz

def ejecutar_cotizador():
    print("=== SISTEMA GERENCIAL DE COTIZACIONES ===")
    
    try:
        # 1. Captura de datos del cliente
        nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
        while not nombre_cliente:
            print(" Error: El nombre no puede estar vacío.")
            nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            
        tipos_cliente = {'A': 'VIP/Mayorista (15%)', 'B': 'Frecuente (10%)', 'C': 'Regular (0%)'}
        print("\nTipos de cliente disponibles:", tipos_cliente)
        tipo_cliente = validaciones.seleccionar_opcion_menu("Seleccione tipo de cliente (A/B/C): ", tipos_cliente)

        # 2. Captura de datos del producto
        nombre_producto = input("\nIngrese la descripción del producto: ").strip()
        while not nombre_producto:
            print(" Error: El producto no puede estar vacío.")
            nombre_producto = input("Ingrese la descripción del producto: ").strip()
            
        precio = validaciones.solicitar_numero_positivo("Ingrese precio unitario ($): ", es_flotante=True)
        cantidad = validaciones.solicitar_numero_positivo("Ingrese cantidad de unidades: ", es_flotante=False)

        # 3. Datos de envío
        zonas_envio = {'1': 'Local ($5.00)', '2': 'Nacional ($10.00)', '3': 'Remota ($20.00)'}
        print("\nZonas de envío disponibles:", zonas_envio)
        zona = validaciones.seleccionar_opcion_menu("Seleccione la zona de envío (1/2/3): ", zonas_envio)

        # 4. Procesamiento mediante funciones del módulo calculos
        subtotal = calculos.calcular_subtotal(precio, cantidad)
        tasa_descuento = calculos.obtener_porcentaje_descuento(tipo_cliente)
        costo_envio = calculos.obtener_costo_envio(zona)
        monto_descuento, total = calculos.calcular_total_cotizacion(subtotal, tasa_descuento, costo_envio)

        # 5. Salida de resultados
        interfaz.mostrar_resumen_cotizacion(
            nombre_cliente, nombre_producto, cantidad, precio,
            subtotal, monto_descuento, costo_envio, total
        )

    except Exception as err:
        print(f"\n Ha ocurrido un error inesperado en el sistema: {err}")

    finally:
        print("Proceso de cotización finalizado.\n")

if __name__ == "__main__":
    ejecutar_cotizador()