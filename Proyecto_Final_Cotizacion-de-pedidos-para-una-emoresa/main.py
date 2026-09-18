import validaciones
import calculos
import interfaz

def run_quotation():
    print("\n--- NUEVA COTIZACIÓN ---")
    total_price = 0.0
    
    try:
        client_name = validaciones.get_valid_text("Ingrese el nombre del cliente: ", is_required=True)
            
        client_types = {'A': 'VIP/Mayorista (15%)', 'B': 'Frecuente (10%)', 'C': 'Regular (0%)'}
        print("\nTipos de cliente disponibles:", client_types)
        client_type = validaciones.select_menu_option("Seleccione tipo de cliente (A/B/C): ", client_types)

        product_list = []
        subtotals = []
        add_more = "S"
        
        while add_more == "S":
            product_name = validaciones.get_valid_text("\nIngrese el nombre del producto: ", is_required=True)
            product_description = validaciones.get_valid_text("Ingrese una breve descripción (opcional, Presione Enter para omitir): ", is_required=False)
                
            price = validaciones.get_positive_number("Ingrese precio unitario (C$): ", is_float=True)
            quantity = validaciones.get_positive_number("Ingrese cantidad de unidades: ", is_float=False)

            item_subtotal = calculos.calculate_subtotal(price, quantity)
            
            if product_description:
                item_detail = f"{product_name} ({product_description}) x{quantity} - C${item_subtotal:.2f}"
            else:
                item_detail = f"{product_name} x{quantity} - C${item_subtotal:.2f}"
                
            product_list.append(item_detail)
            subtotals.append(item_subtotal)

            add_more = validaciones.select_menu_option("¿Desea agregar otro producto? (S/N): ", {'S': 'Sí', 'N': 'No'})

        total_subtotal = calculos.calculate_total_subtotal(subtotals)

        shipping_zones = {'1': 'Local (C$5.00)', '2': 'Nacional (C$10.00)', '3': 'Remota (C$20.00)'}
        print("\nZonas de envío disponibles:", shipping_zones)
        zone = validaciones.select_menu_option("Seleccione la zona de envío (1/2/3): ", shipping_zones)

        discount_rate = calculos.get_discount_rate(client_type)
        shipping_cost = calculos.get_shipping_cost(zone)
        discount_amount, total_price = calculos.calculate_final_total(total_subtotal, discount_rate, shipping_cost)

        interfaz.print_quote_summary(
            client_name, product_list,
            total_subtotal, discount_amount, shipping_cost, total_price
        )

    except Exception as err:
        print(f"\n Ocurrió un error en el sistema: {err}")
        total_price = 0.0

    finally:
        print("Proceso de cotización finalizado.")

    return total_price
def start_app():
    total_quotes = 0
    session_total = 0.0

    while True:
        print("\n=== SISTEMA DE COTIZACIONES ===")
        print("1. Nueva Cotización")
        print("2. Ver Resumen de la Sesión")
        print("3. Salir")
        
        option = validaciones.select_menu_option("Seleccione una opción (1-3): ", {'1': 'Nueva', '2': 'Resumen', '3': 'Salir'})
        
        if option == "1":
            quote_total = run_quotation()
            if quote_total > 0:
                total_quotes += 1
                session_total += quote_total
        elif option == "2":
            print("\n--- RESUMEN DE LA SESIÓN ---")
            print(f" Cotizaciones realizadas: {total_quotes}")
            print(f" Monto total acumulado: C${session_total:.2f}")

        elif option == "3":
            print("\nSaliendo del programa...")
            break

if __name__ == "__main__":
    start_app()