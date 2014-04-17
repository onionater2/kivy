# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:24:12 2014

@author: amyskerry
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        def buttonpress(instance):
            print('The button <%s> is being pressed' % instance.text)
        self.cols = 3
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.button = Button(text='Press me', font_size=14, background_color=[1,1,3,1])
        self.button.bind(on_press=buttonpress)
        self.add_widget(self.button)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.button2 = Button(text='Press me2', font_size=14)
        self.button2.bind(on_press=buttonpress)
        self.add_widget(self.button2)

class MyApp(App):
     def build(self):
         return LoginScreen()

if __name__ == '__main__':
    MyApp().run()