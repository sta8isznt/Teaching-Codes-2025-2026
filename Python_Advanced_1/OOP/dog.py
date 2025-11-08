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

your_dog = Dog("Mike", 10, "black")
print(your_dog.describe_dog())