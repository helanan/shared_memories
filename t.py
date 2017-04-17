class Mary():
    """A simple attempt to model Mary"""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.message = "how are you?"

    def sit(self):
        """Simulate Mary sitting in response to a message."""
        print(self.name.title() + " is now sitting and reading a message.")

    def stand_up(self):
        """Simulate standing up in response to message."""
        print(self.name.title() + " stood up in response to the message!")

    def write_message(self):
        """Return a neatly formated message."""
        new_message = str("Hi" + self.name + "," + " " + self.message + '')
        return mary_message.title()

    def get_message(self):
        """Return a neatly formated message."""
        mary_message = str(self.name + "" + " wrote" + self.message + '')
        return mary_message.title()

my_mary = Mary('Mary', 90)
# your_mary = Mary('Lucy', 67, 'Hi Mary How are you?')
my_new_mary = Mary('Mary', 90)

print("Mary's name is " + my_mary.name.title() + ".")
print("Mary is " + str(my_mary.age) + " years old.")

# print("\nYour name is " + your_mary.name.title() + ".")
# print("Your are " + str(your_mary.age) + " years old.")

print(my_mary.get_message())
print(my_new_mary.get_message())



my_mary.sit()
my_mary.stand_up()
# your_mary.sit()
