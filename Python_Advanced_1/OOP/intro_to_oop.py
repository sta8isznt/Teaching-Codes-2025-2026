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

    def describe_car(self):
        """Return a string that describes our car"""
        return f"I have a {self.make} model {self.model} from {self.year}"

marilena_car = Car("Toyota", "Yaris", 2024)
print(marilena_car.describe_car())

class Dog:
    """A simple attempt to represent a dog"""

    def __init__(self, name, age, skin_color, breed="no breed"):
        self.name = name
        self.age = age
        self.skin_color = skin_color
        self.breed = breed

    def describe_dog(self):
        """Returns a string that describes my dog"""
        return f"My dog is {self.name} and it is {self.age} years old. It has {self.skin_color} skin_color and it is a {self.breed}"

    def sit(self):
        """Tells the dog to sit"""
        print(f"{self.name} sit down!")
    
    def roll_over(self):
        """Tells the dog to roll over"""
        print(f"{self.name} roll over`!")

my_dog = Dog("Rico", 5, "black")
print(my_dog.describe_dog())

