def get_positive_number(prompt, is_float=True):
    while True:
        try:
            entry = input(prompt).strip()
            val = float(entry) if is_float else int(entry)
            if val <= 0:
                print(" Error: El valor debe ser un número mayor a cero.")
                continue
            return val
        except ValueError:
            print(" Error: Debe ingresar un valor numérico válido.")

def select_menu_option(prompt, valid_options):
    while True:
        try:
            option = input(prompt).strip().upper()
            if option not in valid_options:
                raise ValueError("Opción no válida.")
            return option
        except ValueError as e:
            print(f" Error: {e} Elija entre {list(valid_options.keys())}.")

def get_valid_text(prompt, is_required=True):
    while True:
        entry = input(prompt).strip()
        if is_required and not entry:
            print(" Error: Este campo es obligatorio y no puede estar vacío.")
            continue
        return entry