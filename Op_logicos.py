edad= int(input("Ingrese su edad: "))

if edad>=1 and edad<=10:
    print("Usted es un niño")
elif edad>=11 and edad<=17:
    print("Usted es un niño")
else:
    print("Usted es un adulto")

########################################

edad= int(input("Ingrese su edad: "))

if edad==10 or edad==11:
    print("Usted tiene entre 10 y 11 años")
else:
    print("No tengo definicion")

########################################

edad= int(input("Ingrese su edad: "))

if not edad==10:
    print("Usted tiene 10 años")
else:
    print("No tengo definicion")