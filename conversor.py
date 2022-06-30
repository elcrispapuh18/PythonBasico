def conversor (tipo_pesos, valor pesos):
pesos= input ("Cuantos pesos colombianos tienes?")
pesos = float(pesos)
valor_dolar =3875
dolares = pesos / valor_dolar
dolores = round (dolores, 2)
dolares = str(dolores)
print("Tienes $" + dolares + "dolares")

menu = """
Bienvenido al conversor de monedas 

1 - Pesos mexicanos
2 - Pesos colombianos
3 - Pesos argentinos

Elige una opción: """ 

opcion = int(input(menu))

if opcion == 1:
    conversor("mexicanos", 20.34)
elif opcion == 2:
    conversor("colombianos", 3905.90)
elif opcion == 3:
    conversor("argentinos", 123.16)
else:
    print('Ingresa una opción correcta por favor')