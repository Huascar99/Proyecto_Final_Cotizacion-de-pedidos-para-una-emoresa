price = float(input("Dime el precio del producto: "))
desc = float(input("cuanto descuento quiere aplicar al producto: "))

less = price * (desc/100)
total = price - less
print(f" el precio final es de : {total}")
