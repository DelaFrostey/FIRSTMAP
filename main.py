# -*- coding: utf-8 -*-
# from kivy.lang import Builder
# from io import open
from kivymd.app import MDApp
from igormapview import IgorMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper

# with open("main.kv", encoding='utf8') as f:
#     drunk = Builder.load_string(f.read())

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None

    def on_start(self):
        self.theme_cls.primary_palette = "Indigo"
        #GPS
        GpsHelper().run()
        #Конект базы данных
        self.connection = sqlite3.connect("Navigator.sqlite")
        self.cursor = self.connection.cursor()
        #Поисковое меню
        self.search_menu = SearchPopupMenu()

    pass

MainApp().run()