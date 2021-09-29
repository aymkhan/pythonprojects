class Car:
    def __init__(self,company,model,year,price):
        self.company = company
        self.model = model
        self.year = year
        self.price = price

    def getModelYear(self):
        print(self.model + " " + str(self.year))

    def getModel(self):
        return self.model

    def getPrice(self):
        print(self.price)