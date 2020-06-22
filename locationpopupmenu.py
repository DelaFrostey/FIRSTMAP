from kivymd.uix.dialog import ListMDDialog


class LocationPopupMenu(ListMDDialog):
    def __init__(self, shop_data):
        super().__init__()
        # set all of the fields
        headers = "PLID,PLACE_NAME,PART,KM,STREET,TYPE,X,Y,SITE,INFORM"
        headers = headers.split(',')

        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = shop_data[i]
            setattr(self, attribute_name, attribute_value)
