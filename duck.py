class Dog:
    def sound(self):
        print("bowe bowe")
    def walk(self):
        print("it is walk")
class Cat:
    def sound(self):
        print("meaw meaw")
    def walk(self):
        print(" it is walk")
class Duck:
    def sound(self):
        print("quak quak")
    def walk(self):
        print("it is walk")
a=Dog()
b=Cat()
c=Duck()
l=[a,b,c]
def anysound(l):
    for i in l:
        i.walk()
        i.sound()
anysound(l)
