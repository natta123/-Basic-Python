cadena= "Curso de aprendizaje de python"

#Contar una cadena dentro de la cadena
print (cadena.count ("de"))

#Buscar en la cadena mas de una vez
print(cadena.find("de")) #De izq. a der.
print(cadena.rfind("de")) #De der. a izq.

#Devuelve un boolean si la cadeana se encuetra en el inicio de la cadena
print(cadena.startswith("Curso"))
#Devuelve un boolean si la cadeana se encuetra en el final de la cadena
print(cadena.endswith("Curso"))

##################################
numero1="125"
numero2="abc"

#Devuelve boolean si es numerico o no, digito o no en el contenido de la cadena
print(numero1.isnumeric())
print(numero2.isnumeric())
print(numero1.isdigit())
print(numero2.isdigit())

#Devuelve boolean si es alfanumerico o no en el contenido de la cadena
print(numero1.isalnum())

#Devuelve boolean si es alfanumerico o no en el contenido de la cadena
print(numero2.isalpha())

#Ejem. de métodos de análisis de cadenas de caracteres