from kivy.app import App # Importando o app do kivy
from kivy.lang import Builder # Imporando o builder para usar os .kv
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from telas import * # Importando as letras do App
from botoes_extras import * # Importando alguns botões diferentes
from Jogo import Forca # Importando o código do jogo


GUI = Builder.load_file("main.kv") # Definindo o .kv do projeto
class MainApp(App):
    def build(self):
        self.forca = Forca()
        return GUI

    def mudar_tela(self, id_tela):
        gerenciador = self.root.ids["screen_manager"]
        gerenciador.current = id_tela

    def popup_dica(self):
        pagina_jogo = self.root.ids["jogo"]
        # Criar o Popup ao clicar no botão
        popup = Popup(
            title='DICAS: ',
            size_hint=(None, None),
            size=(300, 200),
            auto_dismiss= False
        )
        layout = FloatLayout()
        # Adicionar um texto no popup
        label = Label(text="DICAS CUSTAM 2 TENTATIVAS",
                      size_hint=(None, None),
                      size=(180, 100),
                      font_size = 15,
                      pos_hint={'x': 0.18, 'y': 0.47})

        # Botão de Fechar
        bttn_fechar = ImageButton(source = "fotos/x.png",
                              size_hint=(None, None),
                              size=(70, 30),
                              pos_hint={'x':0.83, 'y': 1.1})
        bttn_fechar.bind(on_press=popup.dismiss)


        # Botão da dica que revela o continente
        bttn_dica_continente = Button(text="NOME DO \nCONTINENTE",
                              size_hint=(None, None),
                              font_size = 20,
                              size=(130, 80),
                              pos_hint={'x': 0, 'y': 0.1})

        # Confere para caso a dica ja tenha sido executada, caso sim, desativa a mesma
        if pagina_jogo.ids.dica_continente.text != "":
            bttn_dica_continente.disabled = True
            # O lambda é necessário para que a função dentro do botão não seja ativada antes do mesmo ser clicado. (padrão do .bind e criação do botão)
        bttn_dica_continente.bind(on_press=lambda instance: self.forca.dica_continente())
        bttn_dica_continente.bind(on_press=popup.dismiss)

        # Botão da dica que revela uma letra
        bttn_dica_letra = Button(text="DESCOBRIR \nUMA LETRA",
                                      size_hint=(None, None),
                                      font_size=20,
                                      size=(140, 80),
                                      pos_hint={'x': 0.5, 'y': 0.1})
        # Confere para caso a dica ja tenha sido executada, caso sim, desativa a mesma
        if pagina_jogo.ids.dica_letra.text != "":
            bttn_dica_letra.disabled = True
        # O lambda é necessário para que a função dentro do botão não seja ativada antes do mesmo ser clicado. (padrão do .bind e criação do botão)
        bttn_dica_letra.bind(on_press=lambda instance:self.forca.dica_letra())
        bttn_dica_letra.bind(on_press=popup.dismiss)

        # Adicionando widgets ao layout
        layout.add_widget(label)
        layout.add_widget(bttn_fechar)
        layout.add_widget(bttn_dica_letra)
        layout.add_widget(bttn_dica_continente)

        # Adicionando o layout ao conteúdo do Popup
        popup.content = layout

        # Abrindo o Popup
        popup.open()

MainApp().run()