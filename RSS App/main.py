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
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivymd.uix.menu import MDDropdownMenu
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
kivy.require('2.1.0')

Window.size = (300,600)

kv = '''
MDBoxLayout:
    orientation: "vertical"
    MDTopAppBar:
        md_bg_color: 255/255.0, 140/255.0, 0/255.0, 1
        title: "RSS"
        left_action_items: [["menu", lambda x: None]]
        right_action_items: [["dots-vertical", lambda x: None]]
        elevation:3   
    GridLayout:
        cols:2
        rows:2
        pos: 100,100
        Button:
            text: "All India"
            #background_color: 255/255.0, 140/255.0, 0/255.0, 1
        Button:
            text: 'Region'
        Button:
            text: 'State'
        Button:
            text: 'District'
    MDBottomAppBar:
        md_bg_color: 255/255.0, 140/255.0, 0/255.0, 1
        MDTopAppBar:
            type: "bottom"
            mode: "center"
            icon: 'help-circle'
            elevation:0  
            on_action_button: app.btn()
            md_bg_color: 255/255.0, 140/255.0, 0/255.0, 1
            icon_color: 255/255.0, 140/255.0, 0/255.0, 1    
            MDFloatingActionButtonSpeedDial:
                label_text_color: "orange"
                data: {"Announcement": "message-alert"}
                rotation_root_button: True
                md_bg_color: 255/255.0, 140/255.0, 0/255.0, 1
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)
    def btn(self):
        popup = Popup(title="About",content=Label(text='''      This application is
    create by Abhay Nath.'''),size_hint=(None,None),size=(200,200))
        popup.open() 
if __name__ == '__main__':        
    MyApp().run()