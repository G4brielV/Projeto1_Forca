from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from telas import *
from botoes import *
from Jogo import Forca

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        self.forca = Forca()
        return GUI

    def mudar_tela(self, id_tela):
        gerenciador = self.root.ids["screen_manager"]
        gerenciador.current = id_tela


MainApp().run()