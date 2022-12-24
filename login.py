import kivy
import kivymd
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.text import LabelBase
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
kivy.require('2.1.0')

Window.size = (300,600)

login = '''
MDFloatLayout:
    md_bg_color: 1,1,1,1
    Image:
        source: "logo.png"
        pos_hint: {"y": 0.25}
    MDLabel:
        text: "Login"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        halign: "center"
        #font_name: "Poppins-SemiBold.ttf"
        font_size: "40sp"
        theme_text_color: "Custom"
        text_color: 60/255, 43/255, 117/255, 1
    MDFloatLayout:
        size_hint: 0.85, 0.08
        pos_hint: {"center_x": 0.5, "center_y": 0.38}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            hint_text: "Email"
            size_hint: 1, None
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0, 0, 0
            padding: 15
            #font_name: "Poppins-SemiBold.ttf"
            font_size: "18sp"
    MDFloatLayout:
        size_hint: 0.85, 0.08
        pos_hint: {"center_x": 0.5, "center_y": 0.28}
        canvas:
            Color:
                rgb: (238/255, 238/255, 238/255, 1)
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [25]
        TextInput:
            hint_text: "Password"
            password: True
            size_hint: 1, None
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            height: self.minimum_height
            multiline: False
            cursor_color: 96/255, 74/255, 215/255, 1
            cursor_width: "2sp"
            foreground_color: 96/255, 74/255, 215/255, 1
            background_color: 0, 0, 0, 0
            padding: 15
            #font_name: "Poppins-SemiBold.ttf"
            font_size: "18sp" 
    MDTextButton:
        text: "Forget your password?"
        #font_name: "Poppins-SemiBold.ttf"
        theme_text_color: "Custom"
        text_color: 246/255, 135/255, 177/255, 1
        pos_hint: {"center_x": 0.5, "center_y": 0.21}
    Button:
        text: "Login"
        #font_name: "Poppins-SemiBold.ttf"
        font_size: "20sp"
        size_hint: 0.5, 0.08
        pos_hint: {"center_x": 0.5, "center_y": 0.12}
        background_color: 0,0,0,0
        canvas.before:
            Color:
                rgb: 246/255, 135/255, 177/255, 1
            RoundedRectangle:
                size: self.size
                pos: self.pos
                radius: [23]
'''

class LoginPage(MDApp):
    def build(self):
        return Builder.load_string(login)
        
if __name__ == "__main__" :
        LoginPage().run()