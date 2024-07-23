from kivy.app import App
from unidecode import unidecode
from Paises import paises
from random import choice

class Forca():
    def __init__(self):
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        pagina_jogo.ids["img_forca"].source = "fotos/forca.png"
        pagina_jogo.ids["letras_usadas"].text = ""
        self.palavra = None
        self.espaco_e_traco = None
        self.vida = 0
        self.letras_usadas = ""
        self.letras_palavra = None

    def achar_pais(self, continente = " "):
        if continente == " ":
            continente = choice(["Africa", "Americas", "Asia", "Europa", "Oceania"])
        self.palavra = choice(paises[continente])
        self.espaco_e_traco = [e for e,p in enumerate(self.palavra) if p in '- ']
        self.letras_palavra = set(unidecode(self.palavra.upper().replace(" ", "").replace("-", "")))
        inicio = ['_' if x not in '- ' else x for x in self.palavra.upper()]
        for posi in self.espaco_e_traco:
            inicio[posi] = self.palavra[posi]
        str_inicio = " ".join(inicio)
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        pagina_jogo.ids["espaco_letras"].text = str_inicio

    def adicionar_letras(self):
        nivel_atual = [self.palavra.upper()[e] if letra in self.letras_usadas else '_' for e,letra in enumerate(unidecode(self.palavra.upper()))]
        for posi in self.espaco_e_traco:
            nivel_atual[posi] = self.palavra[posi]
        str_nivel_atual = " ".join(nivel_atual)
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        pagina_jogo.ids["espaco_letras"].text = str_nivel_atual


    def game(self, chute):
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        chute = unidecode(chute.upper())
        # Zerando o quadro de avisos
        pagina_jogo.ids["aviso"].text = ""
        # Verifcando se é uma letra válida
        if chute.isalpha() and len(chute) == 1:
            # Verificando se a letra ja não foi testada
            if chute in self.letras_usadas:
                pagina_jogo.ids["aviso"].text = f"Voçê ja digitou a letra: {chute}."
            else:
                self.letras_usadas += f" {chute}"
                # print(self.letras_usadas)
                pagina_jogo.ids["letras_usadas"].text = self.letras_usadas
                # Verificando se a letra ta na palavra
                if chute in self.letras_palavra:
                    self.letras_palavra.remove(chute)
                    self.adicionar_letras()
                    # print(self.letras_palavra)
                    if len(self.letras_palavra) == 0:
                        self.ganhou()
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
                        self.perdeu()
        else:
            pagina_jogo.ids["aviso"].text = f'Digite uma letra, "{chute}" não é válido'

    def ganhou(self):
        meu_aplicativo = App.get_running_app()
        pagina_final = meu_aplicativo.root.ids["final"]
        pagina_final.ids["img_final"].source = "fotos/vivo.png"
        pagina_final.ids["text_final"].color = 0, 1, 0
        pagina_final.ids["text_final"].text = "Parabéns"
        pagina_final.ids["msg_final"].text = f"A palavra era: {self.palavra}"
        pagina_final.ids["btn_final"].text = "Recomeçar"
        meu_aplicativo.mudar_tela("final")

    def perdeu(self):
        meu_aplicativo = App.get_running_app()
        pagina_final = meu_aplicativo.root.ids["final"]
        pagina_final.ids["img_final"].source = "fotos/morto.png"
        pagina_final.ids["text_final"].color = 1, 0, 0
        pagina_final.ids["text_final"].text = "Voçê Perdeu!!"
        pagina_final.ids["msg_final"].text = f"A palavra era: {self.palavra}"
        pagina_final.ids["btn_final"].text = "Tentar Novamente"
        meu_aplicativo.mudar_tela("final")


