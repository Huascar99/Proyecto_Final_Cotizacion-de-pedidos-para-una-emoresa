dolar = float(input("Ingresa la cantidad en dólares: "))
change = float(input("Ingresa la tasa de cambio (C$ por USD): "))

cordobas = dolar * change

print(f"La cantidad equivale a: C${cordobas:.2f}")