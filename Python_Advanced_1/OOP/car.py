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

marilena_car = Car("Toyota", "Yaris", 2024)
print(marilena_car.describe_car())
marilena_car.read_odometer()

marilena_car.odometer = 20
marilena_car.read_odometer()

marilena_car.update_odometer(40)
marilena_car.read_odometer()

marilena_car.increment_odometer(20)
marilena_car.read_odometer()
