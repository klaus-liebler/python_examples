class Vehicle:
    def __init__(self, builder):
        self.builder=builder
    def build(self):
        self.takeBaseplate()
        self.buildChassis()
        self.buildBody()
    def takeBaseplate(self):
        print(self.builder + ", nehmen Sie eine geeignete Basisplatte aus der Schachtel.")
    def buildChassis(self):
        print(self.builder + ", bauen Sie zwei Achsen an die Basisplatte")
    def buildBody(self):
        pass

class Sedan(Vehicle):
    def __init__(self, builder):
        super().__init__(builder)
    def buildBody(self):
        print(self.builder + ", bauen Sie eine komfortable Limousinenkarosserie.")

class Cabriolet(Vehicle):
    def __init__(self, builder):
        super().__init__(builder)
    def buildBody(self):
        print(self.builder + ", bauen Sie ein sportliches Cabrio")

class Truck(Vehicle):
    def __init__(self, builder, axis):
        super().__init__(builder)
        self.axis=axis
    def buildChassis(self):
        print(self.builder + ", bauen Sie",self.axis, "Achsen an die Basisplatte")
    def buildBody(self):
        print(self.builder + ", bauen Sie eine Fahrerkabine und einen Spezialaufbau auf.")

list =[Sedan("Karl"), Truck("Kurt", 3), Cabriolet("Kevin") ]
for item in list:
    item.build()