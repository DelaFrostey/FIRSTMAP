from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class OthersMarker(MapMarkerPopup):
    source = "Others.png"
    other_data = []
    def on_release(self):
        #откроем меню
       # LocationPopupMenu(self.cafe_data)
        menu = LocationPopupMenu(self.other_data)
        menu.size_hint = [.7, .9]
        menu.open()