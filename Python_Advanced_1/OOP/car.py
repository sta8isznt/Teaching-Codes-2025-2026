# Αντικειμενοστραφής Προγραμματισμός -> Object Oriented Programming(OOP)

# Τα δύο βασικά πράγματα από τα οποία θα αποτελείται ένα μοντέλο
# είναι τα ΧΑΡΑΚΤΗΡΙΣΤΙΚΑ του και οι ΛΕΙΤΟΥΡΓΙΕΣ του

# Τα χαρακτηριστικά (attributes) τα αποθηκεύουμε σε μεταβλητές
# Τις λειτουργίες (methods) του τις αναπαριστούμε με συναρτήσεις

# Το μοντέλο που θα χρησιμοποιήσουμε είναι η αποτύπωση
# ενός αυτοκινήτου με κώδικα

# Όλα αυτά τα χαρακτηριστικά και τις λειτουργίες τις συγκεντρώνουμε
# μαζί σε μία οντότητα που ονομάζεται κλάση (class)

# Η κλάση είναι ένα γενικό καλούπι!
# Οι υλοποιήσεις της κλάσης ονομάζονται αντικείμενα(objects)
# και έχουν ξεχωριστή ταυτότητα, αλλά υπακούν στους γενικούς
# κανόνες που έχουμε ορίσει στην κλάση.

def add(x, y):
    return x+y

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initilize attributes to describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def describe_car(self):
        """Return a string that describes our car"""
        return f"I have a {self.make} model {self.model} from {self.year}"

    def read_odometer(self):
        """Print a statement showing the car's kilometers"""
        print(f"This car has {self.odometer} kilometers")

    def update_odometer(self, kilometers):
        """Set the odometer to the given value"""
        self.odometer = kilometers

    def increment_odometer(self, kilometers):
        """Add the given amount of kilometers to the odometer"""
        self.odometer += kilometers


class ElectricCar(Car):
    def __init__(self, battery_size, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = battery_size
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}kWh battery")

my_electric_car = ElectricCar(40, "VW", "ID3", 2024)
my_electric_car.describe_battery()
my_electric_car.increment_odometer(10)
my_electric_car.read_odometer()
