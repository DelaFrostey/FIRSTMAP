from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App

class SearchPopupMenu(MDInputDialog):
    title = 'SEARCH BY STREET'
    text_button_ok = 'SEARCH'
    def __init__(self):
        super().__init__()
        self.size_hint = [.9, .3]
        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self,address):
        app_id = 'g3mEMwkUHkRilGjo4xHa'
        app_code = '0KZToCotU6I1qLNm8FasdQ'
        address = parse.quote(address)
        url = "https://geocoder.api.here.com/search/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    def success(self, urlrequest,result):
        print("Success")
        latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
        longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
        #print(result)
        #print(latitude,longitude)
        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude, longitude)

    def error(self, urlrequest,result):
        print("Error")
        print(result)

    def failure(self, urlrequest,result):
        print("Failure ")
        print(result)