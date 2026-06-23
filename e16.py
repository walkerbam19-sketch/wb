compra = int(input("Ingrese el monto de compra: "))
if compra > 100:
    descuento = compra * 10 / 100
    print("Total a pagar:", compra - descuento)
else:
    print("Total a pagar:", compra)