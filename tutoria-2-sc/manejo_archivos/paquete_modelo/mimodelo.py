"""
    creación de clases
"""

class Persona(object):
    """
    """
    
    def __init__(self, n, ape, ed, cod, not1, not2):
        """
        """
        self.nombre = n
        self.edad = int(ed)
        self.codigo = int(cod)
        self.apellido = ape
        self.nota_1 = int(not1)
        self.nota_2 = int(not2)

    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_edad(self, n):
        """
        """
        self.edad = int(n)

    def obtener_edad(self):
        """
        """
        return self.edad
    
    def agregar_codigo(self, n):
        """
        """
        self.codigo = int(n)

    def obtener_codigo(self):
        """
        """
        return self.codigo
    
    def obtener_apellido(self):
        """
        """
        return self.apellido

    def agregar_nota_1(self, not1):
        self.nota_1 = int(not1)

    def obtener_nota_1(self):
        return self.nota_1

    def agregar_nota_2(self, not2):
        self.nota_2 = int(not2)

    def obtener_nota_2(self):
        return self.nota_2

    def __str__(self):
        """
        """
        return "%s - %s - %d - %d - %d - %d" % (self.nombre, self.apellido,\
                self.edad, self.codigo, self.nota_1, self.obtener_nota_2())


class OperacionesPersona(object):
    """
    """
    def __init__(self, listado):
        """
        """
        self.listado_personas = listado
    
    #obtengo el promedio de las notas 1 con un for que me recorre el listado personas
    #y le digo que vaya recorriendo y me vaya acumulando y sumando en SUMA todas las notas 1
    #luego que ese resultado total de la suma de todos los notas 1 me divida para el numero total des estudiantes
    def obtener_promedio_n1(self): 
        suma = 0
        for n in self.listado_personas:
            suma = suma + n.obtener_nota_1()
        promedio = suma/len(self.listado_personas)
        return promedio
    #obtengo el promedio de las notas 2 con un for que me recorre el listado personas
    #y le digo que vaya recorriendo y me vaya acumulando y sumando en SUMA todas las notas 2
    #luego que ese resultado total de la suma de todos las notas2 me divida para el numero total des estudiantes
    def obtener_promedio_n2(self):
        suma = 0
        for n in self.listado_personas:
            suma = suma + n.obtener_nota_2()
        promedio = suma/len(self.listado_personas)
        return promedio

#obtengo el listad de las personas con notas 1 menor a 15, mediante el for recorro la lista y 
#mediante la condicion le digo que solo me imprima los nombres que tienen notas 1 menor a 15
    def obtener_listado_n1(self):
     
        for n in self.listado_personas:
            if(n.nota_1 < 15):
                print(n.nombre)
    
    #obtengo el listad de las personas con notas 2 menor a 15, mediante el for recorro la lista y 
#mediante la condicion le digo que solo me imprima los nombres que tienen notas q menor a 15
    def obtener_listado_n2(self):
     
        for n in self.listado_personas:
            if(n.nota_2 < 15):
                print(n.nombre)
    
    def obtener_promedio(self):
        suma = 0
        for n in self.listado_personas:
            suma = suma + n.obtener_nota_1()
        promedio = suma/len(self.listado_personas)
        return promedio

    def __str__(self):
        """"""
        cadena = ""
        for n in self.listado_personas:
            #cadena = "%s- %s- %s -%d\n" %(cadena , n.obtener_nombre(), n.obtener_apellido())
            cadena = "%d" %(self.obtener_promedio())
            #print(n)
        return cadena