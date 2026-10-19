class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return int(3.14 * self.radius * self.radius)

    def perimeter(self):
        return int(2 * 3.14 * self.radius)

user_input = input("What is the radius of your circle? ")
my_radius = int(user_input) 

my_circle = circle(my_radius)

print("The area is:", my_circle.area())
print("The perimeter is:", my_circle.perimeter())
