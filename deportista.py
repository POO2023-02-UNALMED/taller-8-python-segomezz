from persona import Persona
class Deportista(Persona):
    def __init__(self,nombre,edad,altura,sexo,deporte,añospracticando):
        super().__init__(nombre, edad, altura, sexo)
        self._deporte=deporte
        self._añospracticando=añospracticando
    def getDeporte(self):
        return self._deporte
    def setDeporte(self,deporte):
        self._deporte=deporte
    def getAñosPracticando(self):
        return self._añospracticando
    def setAñosPracticando(self,añospracticando):
        self._añospracticando=añospracticando
