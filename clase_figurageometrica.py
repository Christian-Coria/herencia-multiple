class FiguraGeometrica:
    def __init__(self,alto,ancho):
        self._alto = alto
        self._ancho = ancho

    def __str__(self):
        return "alto: " + self._alto + "ancho: " + self._ancho