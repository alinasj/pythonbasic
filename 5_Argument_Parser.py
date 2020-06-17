
import argparse

parser = argparse.ArgumentParser(description='Process Homes')
parser.add_argument('--name', help='enter name of home owner')
parser.add_argument('--bath', help='enter no. of bathrooms in the house')
parser.add_argument('--bedroom', help='enter no. of bedrooms in the house')
parser.add_argument('--kitchen', help='enter no. of kitchens in the house')

args = parser.parse_args()


# defining my class "house_2"
class house_2:
    # constructor function
    def __init__(self, name, bath_n, bed_n, kitchen_n):
        self.name = name
        self.bath = bath_n
        self.bedroom = bed_n
        self.kitchen = kitchen_n

    # another function inside class
    def print_values(self):
        print("\n",self.name)
        print("no. of baths :", self.bath)
        print("no. of bedrooms :", self.bedroom)
        print("no. of kitchens :", self.kitchen)


# initialized objects with unique values
# object = class (parameters)
fath_2 = house_2("Fath", 5, 10, 5)
srutika_2 = house_2("Srutika" , 5, 1, 3)
aileen_2 = house_2("Aileen", 3, 4, 20)

# accessing function within class
fath_2.print_values()
srutika_2.print_values()
aileen_2.print_values()

# inputs from argparser
user_entered_details = house_2(args.name, args.bath, args.bedroom, args.kitchen )
# call the print function based on user entered details
user_entered_details.print_values()

