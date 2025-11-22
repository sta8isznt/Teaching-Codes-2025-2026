class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_surved = 0

    def show_number_surved(self):
        print(self.number_surved)

    def set_number_surved(self, number_surved):
       self.number_surved = number_surved

my_restaurant = Restaurant("Stathis Restaurant", "Suvlaki")
my_restaurant.show_number_surved()
my_restaurant.set_number_surved(10)
my_restaurant.show_number_surved()