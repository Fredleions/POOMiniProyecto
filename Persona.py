class Persona:
    pass

    def __init__(self, nombre, profesion, sexo, edad):
        self.__nombre = nombre
        self.__profesion = profesion
        self.__sexo = sexo
        self.__edad = edad


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def profesion(self):
        return self.__profesion

    @profesion.setter
    def profesion(self, profesion):
        self.__profesion = profesion

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, sexo):
        self.__sexo = sexo

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def validador(self, edad):
        if edad < 0:
            raise Exception("Edad no puede ser menor a 0")


    def __str__(self):
        return "Nombre: " + str(self.__nombre) + "  Profesion: " + str(self.__profesion) + "  Sexo: " + str(self.__sexo) + " Edad: " + str(self.__edad)


p1 = Persona("Freddy", "Estudiante", "Masculino", 2)

p1.validador(2)

print(p1)