class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_surved = 0

    def show_number_surved(self):
        print(self.number_surved)

    def set_number_surved(self, number_surved):
       self.number_surved = number_surved

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def describe_flavours(self):
        print("We have the following flavours: ")
        for i in self.flavours:
            print(i)

my_icecream_stand = IceCreamStand("O Italos", "Gellato", ["choco", "banana", "vanilla"])
my_icecream_stand.describe_flavours()
