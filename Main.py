import Honda
import Jeep
import Toyota
from Car import Car

print("\nWe have a small inventory of Used and New cars")
choice = input("\nWhich make are you interested in:\nToyota, Jeep, or Honda? ")
choice2 = choice.lower()
print("\nHere are the available cars: ")

if choice2 == "toyota":
    for x in Toyota.toyota:
        Car.getModelYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
    print("You can view more cars at the dealer's website ")
    print("https://toyota.com")
    # Provide more information about the user selected car
    #car_choice = input("Which one would you like to see more info about? ")
    #for x in Toyota.toyota:
    #    if car_choice == str(Car.getModel(x[0])):
    #        print("Corolla - good choice!")
    # end of comment
elif choice2 == "honda":
    for x in Honda.honda:
        Car.getModelYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
    print("You can view more cars at the dealer's website ")
    print("https://www.honda.com")
elif choice2 == "jeep":
    for x in Jeep.jeep:
        Car.getModelYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
    print("You can view more cars at the dealer's website ")
    print("https://www.jeep.com")
else:
    print("Woops, nevermind. You did not make a valid selection.\nEnd of program. ")
    exit()





