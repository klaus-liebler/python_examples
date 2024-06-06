class MyClass:
    def __init__(self, x_von_außen):
        self.x = x_von_außen
    def increment(self):
        self.x+=1
    def tell_me(self):
        print("Es gilt ",(self.x)-1, "< Zahl <", (self.x)+1)

my_object1 = MyClass(1)
my_object10 = MyClass(10)
my_object10.increment()
my_object1.increment()
my_object1.tell_me()
my_object10.tell_me()
    
