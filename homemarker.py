from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class HomeMarker(MapMarkerPopup):
    source = "home.png"
    home_data = []
    def on_release(self):
        pass
        #откроем меню
