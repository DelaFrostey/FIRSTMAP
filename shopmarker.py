from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class ShopMarker(MapMarkerPopup):
    source = "shop.png"
    shop_data = []
    def on_release(self):
        #откроем меню
        menu = LocationPopupMenu(self.shop_data)
        menu.size_hint = [.7, .9]
        menu.open()
