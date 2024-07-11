from kivy.app import App
from kivy.lang import Builder
from telas import *
from botoes import *

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI

    def mudar_tela(self, id_tela):
        gerenciador = self.root.ids["screen_manager"]
        gerenciador.current = id_tela


MainApp().run()