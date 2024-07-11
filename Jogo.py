from Paises import paises
from random import choice

class Forca():
    def __init__(self):
        self.palavra = None

    def achar_pais(self, continente = " "):
        if continente == " ":
            continente = choice(["Africa", "Americas", "Asia", "Europa", "Oceania"])
        self.palavra = choice(paises[continente])
    def game(self):
        vida = 0
        ganhou = False
        letras_palavra = set(self.palavra.upper().replace(" ", "").replace("-", ""))
        print(letras_palavra)
        letras_usadas = set()
        while vida < 7 and not ganhou:
            letra = str(input("Digite uma letra: ")).upper()
            if letra.isalpha() and len(letra) == 1:
                if letra in letras_usadas:
                    print("Voçê ja digitou essa letra.")
                elif letra in letras_palavra:
                    letras_usadas.add(letra)
                    letras_palavra.remove(letra)
                    if len(letras_palavra) == 0:
                        ganhou = True
                else:
                    vida += 1
            else:
                print(f'Digite uma letra, "{letra}" não é válido')
        if ganhou:
            print("Parabéns")
        else:
            print(f"Voçê perdeu, a palavra correta era: {self.palavra}")

if __name__ == '__main__':
    jogo = Forca()
    jogo.achar_pais()
    jogo.game()
