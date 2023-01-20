# day07

class Animal:
    def says(self):
        return "I speak!"


class Horse:
    def says(self):
        return "Neigh!"


class Donkey:
    def says(self):
        return "Hee-haw!"


class Mule(Donkey, Horse):
    pass


class Hinny(Horse, Donkey):
    pass


h1 = Hinny()
m1 = Mule()
print(h1.says())    # Horse에서 says 객체를 먼저 찾는다.
print(m1.says())    # Donkey에서 says 객체를 먼저 찾는다.

