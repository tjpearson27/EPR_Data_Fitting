#kivytest

import kivy

from kivy.app import App 
from kivy.uix.button import Label

class HelloKivy(App):
    def build(self):
        return Label(text="genius")

helloKivy = HelloKivy()
helloKivy.run()