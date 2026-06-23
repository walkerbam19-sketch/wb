n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
oper = input("Ingrese la operación (+, -, *, /): ")
if oper == "+":
    print("Resultado:", n1 + n2)
elif oper == "-":
    print("Resultado:", n1 - n2)
elif oper == "*":
    print("Resultado:", n1 * n2)
elif oper == "/":
    print("Resultado:", n1 / n2)
else:
    print("Operación no válida")