contenido= ["Cursos","Alumnos",1025,True,105.38]
print (contenido)

#Cambiar contenido de la lista
contenido[1]= "Estudiantes"
print (contenido)

#Imprimir contenido determiando
print(contenido[3])

#Imprimir ultimo elemento de la lista
print(contenido[-1])

#Imprimir determiandos elementos
print(contenido[0:3])

#Imprimir contenido determinado desde la pos. 0
print(contenido[:2])

#Agregar contenido a la lista
contenido.append("Python")
print(contenido)

#Agregar contenido en determinada posicion
contenido.insert(2,"Profesor")
print(contenido)

#Agregar mas de 1 elemento
contenido.extend(["Nivel basico","Nivel avanzado","Nivel intermedio"])
print(contenido)

#Consultar donde se encuentra el contenido
print(contenido.index("Python"))

#Eliminar contenido determiando
contenido.remove("Cursos")
print(contenido)

#Devuelve numero de veces que se ha encontrado un contenido o no
print(contenido.count(1025))
contenido.append(1025)
contenido.append(1025)
print(contenido)
print(contenido.count(1025))

#Combinar 2 listas
contenido2=["Curso1","Curso 2"]
resultado=contenido+contenido2
print(resultado)
