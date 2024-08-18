'''
#Input del usuario
pesoscol = input("¿Cuantos pesos colombianos tienes ?")
pesoscol = float(pesoscol)
#Declaracion de valores
valor_dolar = 3679
valor_euro = 4383
valor_cake = 58800
valor_btc = 136134100
#Calculo valor dolar
dolares= pesoscol / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
#Calculo Valor Euro
euros= pesoscol / valor_euro
euros = round(euros, 2)
euros = str(euros)
#Calculo Cantidad de CAKE
cakes = pesoscol / valor_cake
cakes = round(cakes, 4)
cakes = str(cakes)
#Calculo Bitcoin
btcs = pesoscol / valor_btc
btcs = round(btcs, 9)
btcs = str(btcs)
#Prints
print("Tienes $"+ dolares + " dolares")
print("Tienes $"+ euros + " Euros")
print("Tienes: " + cakes + " CAKE")
print("Tienes: " + btcs + " Bitcoins")
'''

# Metodos:
# variable.upper() = 'todos los caracteres en MAYÚSCULAS'
# variable.lower() = 'todos los caracteres en minúscula'
# variable.capitalize() = 'solo la primera en MAYÚSCULA'
# variable.strip() = 'eliminar espacios basura del string'
# variable.replace('caractera a cambiar', 'caracter por poner') = remplazar caracter
# FUNCIONES BILT IN
# aquellas que son propias del lenguaje y que no tenemos que crearlas, solo invocarlas.
# len()
# print()
# input()


def conversor(tipo_soles, valor_dolar):
    soles = float(input("¿Cuántos " + tipo_soles + " tienes?: "))
    dolares = soles / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + "dólares")

menu = """ 
Bienvenido al conversor de monedas ❤  
1 - Soles Peruanos
2 - Pesos Colombianos
3 - Pesos Mexicanos

Elige una opción: """

opcion=int(input(menu))
if opcion==1:
    conversor("soles peruanos", 4)
elif opcion ==2:
    conversor("pesos colombianos", 3875)
elif opcion == 3:
    conversor("pesos mexicanos", 65)
else:
    print("Ingrese una opcion correcta")