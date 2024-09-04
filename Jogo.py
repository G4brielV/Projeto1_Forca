from kivy.app import App # Importar o app do kivy para o codigo
from unidecode import unidecode # Tratar os acentos e ç
from Paises import paises # "Banco de dados" com todos os nomes dos paises
from random import choice # Randomizar a escolha dos paises

class Forca():
    def __init__(self):
        '''Zerando as telas para o inicio/reinicio'''
        meu_aplicativo = App.get_running_app() # Puxando o App para conseguir edita-lo
        pagina_jogo = meu_aplicativo.root.ids["jogo"] # Selecionando a tela pelo id
        pagina_jogo.ids["img_forca"].source = "fotos/forca.png"  # Mudando a imagem da página
        pagina_jogo.ids["letras_usadas"].text = "" # Zerando a label

        self.palavra = None # A palavra sorteada
        self.vida = 0 # Quantidade de vida do jogador
        self.letras_usadas = "" # Todas as letras ja testadas
        self.letras_palavra = None # Todas as letras da palavra, sem repetições, acentos ou caractere especial

        lista = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
                 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
                 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
        for btn in lista:
            pagina_jogo.ids[f"{btn}"].disabled= False

    # Sortear o paísc
    def achar_pais(self, continente = " "):
        # Caso ele escolha "Todos os países"
        if continente == " ":
            continente = choice(["Africa", "Americas", "Asia", "Europa", "Oceania"])
        self.palavra = choice(paises[continente]) # Sorteando o pais
        self.letras_palavra = set(unidecode(self.palavra.upper().replace(" ", "").replace("-", "")))
        self.text_inicio()

    # Criar o texto inicial da tela do jogo
    def text_inicio(self):
        # Criando o primeiro texto do jogo, com os devidos espaços e " - "
        inicio = ['_' if x not in '- ' else x for x in self.palavra.upper()]
        str_inicio = " ".join(inicio) # tranformando em str, para o kivy aceitar

        # Modificando o texto na tela
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        pagina_jogo.ids["espaco_letras"].text = str_inicio

    # Atualizar a palavra na tela do jogo com os acertos
    def adicionar_letras(self):
        nivel_atual = [self.palavra.upper()[e] if letra in self.letras_usadas or letra in '- ' else '_' for e,letra in enumerate(unidecode(self.palavra.upper()))]
        str_nivel_atual = " ".join(nivel_atual)

        # Modificando o texto na tela
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        pagina_jogo.ids["espaco_letras"].text = str_nivel_atual

    # Funcionalidades padrões do jogo
    def tentar_letra(self, chute):
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]
        chute = unidecode(chute.upper())

        pagina_jogo.ids[f'{chute}'].disabled = True
        if (len(self.letras_usadas)//2) % 5 == 0:
            self.letras_usadas += '\n'
        self.letras_usadas += f" {chute}"
        pagina_jogo.ids["letras_usadas"].text = self.letras_usadas
        # Verificando se existe a letra chutada na palavra
        if chute in self.letras_palavra:
            self.letras_palavra.remove(chute)
            self.adicionar_letras()
            # Verificando se todas as letras ja foram acertadas
            if len(self.letras_palavra) == 0:
                self.ganhou()
        else:
            # Perde uma vida
            self.vida += 1
            # Mudando a imagem de acordo com a vida
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
                pagina_jogo.ids["img_forca"].source = "fotos/boneco_2_braco.png"
            elif self.vida == 7:
                self.perdeu()

    def tentar_palavra(self, chute_palavra):
        meu_aplicativo = App.get_running_app()
        pagina_jogo = meu_aplicativo.root.ids["jogo"]

        # Zerando a caixa de chute da palavra
        pagina_jogo.ids["chute_palavra"].text = ""

        if unidecode(chute_palavra.upper().strip()) == unidecode(self.palavra.upper()):
            self.ganhou()
        else:
            self.perdeu()


    # Atualizar a tela final para o cenário de vencedor
    def ganhou(self):
        meu_aplicativo = App.get_running_app()
        pagina_final = meu_aplicativo.root.ids["final"]

        pagina_final.ids["img_final"].source = "fotos/vivo.png"
        pagina_final.ids["text_final"].color = 0, 1, 0
        pagina_final.ids["text_final"].text = "Parabéns"
        pagina_final.ids["msg_final"].text = f"A palavra era: {self.palavra}"
        pagina_final.ids["btn_final"].text = "Recomeçar"
        meu_aplicativo.mudar_tela("final")

    # Atualizar a tela final para o cenário de perdedor
    def perdeu(self):
        meu_aplicativo = App.get_running_app()
        pagina_final = meu_aplicativo.root.ids["final"]

        pagina_final.ids["img_final"].source = "fotos/morto.png"
        pagina_final.ids["text_final"].color = 1, 0, 0
        pagina_final.ids["text_final"].text = "Voçê Perdeu!!"
        pagina_final.ids["msg_final"].text = f"A palavra era: {self.palavra}"
        pagina_final.ids["btn_final"].text = "Tentar Novamente"
        meu_aplicativo.mudar_tela("final")


