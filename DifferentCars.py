from Car import Car

toyota1 = Car("Toyota","Corolla",1998,"$8000")
toyota2 = Car("Toyota","Camry", 2001,"$14,600")
toyota3 = Car("Toyota","Odyssey",2020,"37,000")

toyota = (toyota1,toyota2,toyota3)

honda1 = Car("Honda","Civic",2012,"$23,000")
honda2 = Car("Honda","CR-V",2015,"$34,000")

honda = (honda1,honda2)

jeep1 = Car("Jeep","Wrangler",2021,"$47,000")
jeep2 = Car("Jeep","SomeJeep",1996,"$15,900")

jeep = (jeep1,jeep2)

print("\nWe have a small inventory of Used and New cars")
choice = input("\nWhich make are you interested in:\nToyota, Jeep, or Honda? ")
choice2 = choice.lower()
print("\nHere are the available cars: ")

if choice2 == "toyota":
    for x in toyota:
        Car.getModelYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
    print("You can view more cars at the dealer's website ")
    print("https://toyota.com")
    # Provide more information about the user selected car
    car_choice = input("Which one would you like to see more info about? ")
    for x in toyota:
        if car_choice == str(Car.getModel(x[0])):
            print("Corolla - good choice!")
    # end of comment
elif choice2 == "honda":
    for x in honda:
        Car.getModelYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
    print("You can view more cars at the dealer's website ")
    print("https://www.honda.com")
elif choice2 == "jeep":
    for x in jeep:
        Car.getModelYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
    print("You can view more cars at the dealer's website ")
    print("https://www.jeep.com")
else:
    print("Woops, nevermind. You did not make a valid selection.\nEnd of program. ")
    exit()





