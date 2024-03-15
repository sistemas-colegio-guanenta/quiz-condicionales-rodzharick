# Quiz instrucciones condicionales
"""Dados tres números a, b y c, correspondientes a la longitud de los lados de una figura geométrica, determinar si pueden formar los lados de un triángulo."""

print("------------------------------")
print("----- VERIFICAR TRIANGULO ----")
print("------------------------------")

# input
a = float(input("Ingrese el digito del lado a: "))
b = float(input("Ingrese el digito  del lado b: "))
c = float(input("Ingrese el digito del lado c: "))

# processing
es_triangulo = a + b > c and a + c > b and b + c > a

# output
if es_triangulo:
    print(f"Estas longitudes ({a}, {b}, {c}) pueden formar un triángulo.")
else:
    print(f"Estas longitudes ({a}, {b}, {c}) no pueden formar un triángulo.")
