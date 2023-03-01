#Arreglo de datos ordenados, dado por llave y valor
persona={"nombre":"Natanael","Apellido":"Barone","edad":30, "sueldo": 2020.45}
print(persona)

#Mostrar por clave 
print(persona["sueldo"])

#Modificar un valor
persona["edad"]= 31
print(persona)

#Eliminar un valor
del persona["edad"]
print(persona)

#Consultar si existe un valor
print(persona.get("Apellidos","Clave no encontrada"))
print(persona.get("Apellido","Clave no encontrada"))

#Mostrar claves del diccionario
print(persona.keys())

#Mostrar valores del diccionario
print(persona.values())

#Ejer. de manipulacion de diccionario
