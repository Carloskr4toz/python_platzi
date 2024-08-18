'''
#Condicionales:
edad = int(input("Escribe tu edad: "))
if(edad >= 18):
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")
'' 
n = int(input("Escribe un número: "))
if (n>5):
    print("Es mayor a 5.")
elif (n==5):
    print("Es igual a 5.")   
else: 
    print("Es menor a 5.")
'''
nacionalidad = input("¿Eres peruano? (Responde sí o no): ")
if nacionalidad == "sí":
    cambio_a_soles = 3.9865
    dolares = str(round(float(input("¿Cuántos soles tienes? "))/cambio_a_soles, 2))
    print("Entonces tienes " + dolares + " dólares.")
elif nacionalidad == "no":
    cambio_a_dolares = 0.25298
    soles = str(round(float(input("Bienvenido a Perú. ¿Cuántos dólares tienes? "))/cambio_a_dolares, 2))
    print("Entonces tienes " + soles + " soles.")
else:
    print("Escribe sólo sí o no, por favor. ")