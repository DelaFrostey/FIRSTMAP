from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class EnterMarker(MapMarkerPopup):
    source = "enter.png"
    enter_data = []
    def on_release(self):
        #откроем меню
        menu = LocationPopupMenu(self.enter_data)
        menu.size_hint = [.7, .9]
        menu.open()