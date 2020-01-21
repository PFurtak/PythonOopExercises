from pprint import pprint

# You are given this person class


class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends =

    def greet(self, other_person):
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
# Go back to the Person class. Add a print_contact_info method to the Person class
#  that will print out the contact info for a object instance of Person.
# You will use it thus:
# >>> sonny.print_contact_info()
# Sonny's email: sonny@hotmail.com, Sonny's phone number: 483-485-4948

    def print_info_two(self):
        return "{}'s email: {}, {}'s phone number: {} ".format(self.name, self.email, self.name, self.phone)


print('*******************************')
# Instantiate an instance object of Person with name of 'Sonny',
# email of 'sonny@hotmail.com', and phone of '483-485-4948',
# store it in the variable sonny.
sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

# Instantiate another person with the name of 'Jordan',
#  email of 'jordan@aol.com', and phone of '495-586-3456',
#  store it in the variable 'jordan'.
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')


# Have sonny greet jordan using the greet method.
sonny.greet(jordan)
# Have jordan greet sonny using the greet method.
jordan.greet(sonny)
# Write a print statement to print the contact info (email and phone) of Sonny
pprint(vars(sonny))
# Write another print statement to print the contact info of Jordan.
pprint(vars(jordan))
print(sonny.print_info_two())
print(jordan.print_info_two())
print('*******************************')

# Create a class Vehicle. A Vehicle object will have 3 attributes: make, model, year.


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Add a print_info method to the Vehicle class. It will print out the vehicle's information like so:
# >>> car.print_info() 2015 Nissan Leaf

    def print_info(self):
        return "{} {} {}".format(self.year, self.make, self.model)


car = Vehicle('Mazda', 'RX-7', '1993')
print(car.print_info())
