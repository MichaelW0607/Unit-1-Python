class person:
    species = "Homosapien"
    def hello(self):
        print("hello world")

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def hi(self):
        print("Hi my name is" + self.name)
michael = person("michael",17)
print(michael.name)
print(michael.age)
michael.hi
print(michael.species)
michael.hello()
moinul = person("moinul",17)
print(moinul.name)
print(moinul.age)
    