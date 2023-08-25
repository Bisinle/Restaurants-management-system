class Restaurant:
    def __init__(self, name="CJ"):
        self._name = ""
        if isinstance(name, str):
            self._name = name
        else:
            print("Restaurant name must be a string")

    def get_name(self):
        print("----------------")
        return self._name


restaurant1 = Restaurant("Alabasta")
print(restaurant1.get_name())
