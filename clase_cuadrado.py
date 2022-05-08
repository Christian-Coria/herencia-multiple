from ast import Return
from clase_figurageometrica import *
from clase_color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self,color,lado):
        FiguraGeometrica().__init__(self,lado,lado)
        Color().__init__(self,color)
        

    def calculando_area(self):
        area = self._alto * self._ancho
        return area
        
