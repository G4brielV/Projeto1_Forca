from kivy.app import App

from Paises import paises
from random import choice

class Forca():
    def __init__(self):
        self.palavra = None
        self.vida = 0
        self.ganhou = False
        self.letras_usadas = ""
        self.letras_palavra = None

    def achar_pais(self, continente = " "):
        if continente == " ":
            continente = choice(["Africa", "Americas", "Asia", "Europa", "Oceania"])
        self.palavra = choice(paises[continente])
        print(self.palavra)
        self.letras_palavra = set(self.palavra.upper().replace(" ", "").replace("-", ""))
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        pagina_jogo.ids["espaco_letras"].text = " _ "*len(self.palavra.replace(" ", "").replace("-", ""))
        print(pagina_jogo.ids["espaco_letras"].text)

    def adicionar_letras(self):
        nivel_atual = [letra if letra in self.letras_usadas else '_' for letra in self.palavra.upper()]
        str_nivel_atual = " ".join(nivel_atual)
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        pagina_jogo.ids["espaco_letras"].text = str_nivel_atual


    def game(self, chute):
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        # Verifcando se é uma letra
        if chute.isalpha() and len(chute) == 1:
            chute = chute.upper()
            # Verificando se a letra ja não foi testada
            if chute in self.letras_usadas:
                pagina_jogo.ids["aviso"].text = f"Voçê ja digitou a letra: {chute}."
            else:
                self.letras_usadas += f" {chute}"
                print(self.letras_usadas)
                pagina_jogo.ids["letras_usadas"].text = self.letras_usadas
            # Verificando se a letra ta na palavra
            if chute in self.letras_palavra:
                self.letras_palavra.remove(chute)
                self.adicionar_letras(chute)
                print(self.letras_palavra)
                if len(self.letras_palavra) == 0:
                    meu_aplicativo.mudar_tela("final")
            # Se a letra não estive na palavra
            else:
                # Perde uma vida
                self.vida += 1
                # Mudando a imagem
                if self.vida == 1:
                    pagina_jogo.ids["img_forca"].source = "fotos/boneco_cabeca.png"
                elif self.vida == 2:
                    pagina_jogo.ids["img_forca"].source = "fotos/boneco_tronco.png"
                elif self.vida == 3:
                    pagina_jogo.ids["img_forca"].source = "fotos/boneco_1_perna.png"
                elif self.vida == 4:
                    pagina_jogo.ids["img_forca"].source = "fotos/boneco_2_perna.png"
                elif self.vida == 5:
                    pagina_jogo.ids["img_forca"].source = "fotos/boneco_1_braco.png"
                elif self.vida == 6:
                    pagina_jogo.ids["img_forca"].source = "fotos/boneco_2_perna.png"
                    meu_aplicativo.mudar_tela("final")
        else:
            print(f'Digite uma letra, "{chute}" não é válido')


if __name__ == '__main__':
    jogo = Forca()
    jogo.achar_pais()
    jogo.game()
