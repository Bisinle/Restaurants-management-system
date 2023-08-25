class Restaurant:
    def __init__(self, name="CJ"):
        self._name = ""
        if isinstance(name, str):
            self._name = name
        else:
            print("Restaurant name must be a string")

    def get_name(self):
        return self._name


restaurant1 = Restaurant("Alabasta")
restaurant2 = Restaurant("Konoha")
restaurant3 = Restaurant("Sky_land")
# print(restaurant1.get_name())
