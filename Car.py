class Car:
    def __init__(self,company,model,year,price):
        self.company = company
        self.model = model
        self.year = year
        self.price = price

    def getNameYear(self):
        print self.model + " " + str(self.year)

    def getPrice(self):
        print self.price