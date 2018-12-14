from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()#lee el archivo

lista = m.obtener_informacion()#obtiene la informacion del archivo
lista = [l.split("|") for l in lista]#separador de los datos
# print(lista)
lista_personas =[]#arreglo de personas
lista = lista[1:]
# p = Persona(lista[1][1], lista[1][2], lista[1][3], lista[1][0])

for d in lista:#me recorre el listado de personas
    # print(d)
   # suma_n1 = suma_n1 + int(d[4])
    p = Persona(d[1], d[2], d[3], d[0], d[4], d[5])
    lista_personas.append(p)

operaciones = OperacionesPersona(lista_personas)
print(operaciones.obtener_promedio())

#llamo a los metodos de mimodelo
print("Promedio de las Notas 1")
print(operaciones.obtener_promedio_n1())
print("Promedio de las Notas 2")
print(operaciones.obtener_promedio_n2())
print("listado de las Notas 1 menor a 15")
print(operaciones.obtener_listado_n1())
print("listado de las Notas 2 menor a 15")
print(operaciones.obtener_listado_n2())

