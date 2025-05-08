# ESCRIBE ESTA LINEA DE CODIGO
print("Bienvenidos al entrenamiento con python, vamos a disfrutar al maximo esta sesion")
"""
descuento en una compra:
si compras mas de $1000 optienes un descuento del 20%
pide el monto de la compra y muestra el precio final
"""
# pedir datos por teclado al ususario imt (entero) float (decimales) str (cadenas de caracteres) bool (boleano)

compra = float(input("por favor digita el valor de tu compra: "))
# si compras mas de $1000, obtienes un descuento del 20%.
# siempre que la salida tenga mas de un camino de resolución, debo implementar condicionales
# operadores combinados
# operadores de asignación =, operadores aritmeticos + - * /,operadores logicos and y, or o, not
# operadores de comparación ==,!=,>,<,>=,<=

if compra > 1000: 
   descuento = compra * 0.2
   compra -= descuento
   #compra = compra - descuento
   print(f"el descuento es de {descuento}, por lo tanto su valor a pagar es: {compra}")             