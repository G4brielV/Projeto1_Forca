from kivy.app import App # Importando o app do kivy
from kivy.lang import Builder # Imporando o builder para usar os .kv
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
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




MainApp().run()