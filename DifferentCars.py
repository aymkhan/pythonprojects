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
choice = raw_input("\nWhich make are you interested in?\nToyota, Jeep, or Honda? ")
choice2 = choice.lower()
print(choice2)
print("\nHere are the available cars: ")

if choice2 == "toyota":
    for x in toyota:
        Car.getNameYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
elif choice2 == "honda":
    for x in honda:
        Car.getNameYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
elif choice2 == "jeep":
    for x in jeep:
        Car.getNameYear(x)
        print("priced at: ")
        Car.getPrice(x)
        print("\n")
else:
    print("You did not make a valid selection ")

print("End of program.")
