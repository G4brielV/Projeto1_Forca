from Paises import paises
from random import choice

class Forca():
    def __init__(self):
        self.palavra = None

    def achar_pais(self, continente = " "):
        if continente == " ":
            continente = choice(["Africa", "Americas", "Asia", "Europa", "Oceania"])
        self.palavra = choice(paises[continente])



if __name__ == '__main__':
    Forca.achar_pais("a")
