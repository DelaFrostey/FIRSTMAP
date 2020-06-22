from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class CafeMarker(MapMarkerPopup):
    source = "cafe.png"
    cafe_data = []
    def on_release(self):
       # LocationPopupMenu(self.cafe_data)
        menu = LocationPopupMenu(self.cafe_data)
        menu.size_hint = [.7, .9]
        menu.open()

