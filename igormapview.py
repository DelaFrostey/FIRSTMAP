from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from shopmarker import ShopMarker
from cafesmarker import CafeMarker
from entermarker import EnterMarker
from othersmarker import OthersMarker
from homemarker import HomeMarker

class IgorMapView(MapView):
    getting_markets_timer = None
    getting_markets_timer2 = None
    getting_markets_timer3 = None
    getting_markets_timer4 = None
    shop_names = []

    def start_getting_markets_in_iov(self):
        #После 1 секунды получать объекты в поле видимости
        try:
            self.getting_markets_timer.cancel()
            self.getting_markets_timer2.cancel()
            self.getting_markets_timer3.cancel()
            self.getting_markets_timer4.cancel()
        except:
            pass
        self.getting_markets_timer = Clock.schedule_once(self.get_markets_in_iov, 1)
        self.getting_markets_timer2 = Clock.schedule_once(self.get_markets_in_iov2, 1)
        self.getting_markets_timer3 = Clock.schedule_once(self.get_markets_in_iov3, 1)
        self.getting_markets_timer4 = Clock.schedule_once(self.get_markets_in_iov4, 1)


    def get_markets_in_iov(self, *args):
        #Получим
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        zapros = "SELECT * FROM Places WHERE typeM = 'Shop' ORDER BY id"
        app.cursor.execute(zapros)
        shops = app.cursor.fetchall()
        #print(shops)
        #print(self.get_bbox())
        for shop in shops:
            name = shop[1]
            if name in self.shop_names:
                continue
            else:
                self.add_shop(shop)

    def add_shop(self, shop):
        #Создадим маркер магазина
        lat, lon = shop[6], shop[7]
        marker = ShopMarker(lat=lat, lon=lon)
        marker.shop_data = shop
        #Добавим маркер магазина на карту
        self.add_widget(marker)
        #Отследим имена маркеров
        name = shop[1]
        self.shop_names.append(name)

    def get_markets_in_iov2(self, *args):
        #Получим
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        zapros2 = "SELECT * FROM Places WHERE typeM = 'Cafes' ORDER BY id"
        app.cursor.execute(zapros2)
        cafes = app.cursor.fetchall()
        #print(self.get_bbox())
        for cafe in cafes:
            self.add_cafe(cafe)
        self.go_home()

    def add_cafe(self, cafe):
        #Создадим маркер магазина
        lat, lon = cafe[6], cafe[7]
        marker = CafeMarker(lat=lat, lon=lon)
        marker.cafe_data = cafe
        #Добавим маркер магазина на карту
        self.add_widget(marker)
        #Отследим имена маркеров

    def get_markets_in_iov3(self, *args):
        #Получим
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        zapros3 = "SELECT * FROM Places WHERE typeM = 'Entertainment' ORDER BY id"
        app.cursor.execute(zapros3)
        enters = app.cursor.fetchall()
        #print(self.get_bbox())
        for enter in enters:
            self.add_enter(enter)

    def add_enter(self, enter):
        #Создадим маркер магазина
        lat, lon = enter[6], enter[7]
        marker = EnterMarker(lat=lat, lon=lon)
        marker.enter_data = enter
        #Добавим маркер магазина на карту
        self.add_widget(marker)
        #Отследим имена маркеров

    def get_markets_in_iov4(self, *args):
        #Получим координаты
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        zapros4 = "SELECT * FROM Places WHERE typeM = 'Others' ORDER BY id"
        app.cursor.execute(zapros4)
        others = app.cursor.fetchall()
        #print(self.get_bbox())
        for other in others:
            self.add_other(other)

    def add_other(self, other):
        #Создадим маркер магазина
        lat, lon = other[6], other[7]
        marker = OthersMarker(lat=lat, lon=lon)
        marker.other_data = other
        #Добавим маркер магазина на карту
        self.add_widget(marker)
        #Отследим имена маркеров

    def go_home(MapMarkerPopup):
        source = "home.png"
        lat = 61.691962
        lon = 50.807957
        marker = HomeMarker(lat=lat, lon=lon)
        MapMarkerPopup.add_widget(marker)

