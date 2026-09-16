def solicitar_numero_positivo(mensaje, es_flotante=True):
    """Solicita un número y valida que sea mayor a cero."""
    while True:
        try:
            entrada = input(mensaje)
            valor = float(entrada) if es_flotante else int(entrada)
            if valor <= 0:
                print(" Error: El valor debe ser mayor a cero.")
                continue
            return valor
        except ValueError:
            print(" Error: Debe ingresar un valor numérico válido.")

def seleccionar_opcion_menu(mensaje, opciones_validas):
    """Garantiza que la opción seleccionada pertenezca a la lista de opciones permitidas."""
    while True:
        try:
            opcion = input(mensaje).strip().upper()
            if opcion not in opciones_validas:
                raise ValueError("Opción no válida.")
            return opcion
        except ValueError as e:
            print(f" Error: {e} Elija entre {list(opciones_validas.keys())}.")