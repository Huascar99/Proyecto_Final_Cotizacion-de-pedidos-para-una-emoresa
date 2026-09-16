def calcular_subtotal(precio, cantidad):
    """Calcula el subtotal base del producto."""
    return precio * cantidad

def obtener_porcentaje_descuento(tipo_cliente):
    """Determina el porcentaje de descuento basado en la categoría del cliente."""
    descuentos = {
        'A': 0.15,  # Cliente VIP / Mayorista: 15%
        'B': 0.10,  # Cliente Frecuente: 10%
        'C': 0.00   # Cliente Regular: 0%
    }
    return descuentos.get(tipo_cliente, 0.0)

def obtener_costo_envio(zona):
    """Determina el costo de envío según la zona geográfica."""
    costos_envio = {
        '1': 5.00,   # Zona Local
        '2': 10.00,  # Zona Nacional
        '3': 20.00   # Zona Internacional / Remota
    }
    return costos_envio.get(zona, 0.0)

def calcular_total_cotizacion(subtotal, tasa_descuento, costo_envio):
    """Calcula el monto de descuento y el total final."""
    monto_descuento = subtotal * tasa_descuento
    subtotal_con_descuento = subtotal - monto_descuento
    total_final = subtotal_con_descuento + costo_envio
    return monto_descuento, total_final