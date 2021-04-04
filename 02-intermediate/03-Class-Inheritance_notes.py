class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("inhale, exhale")


class Fish(Animal):
    def __init__(self):
        # makes child inherit the __init__ method from parent
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing underwater")

    def swim(self):
        print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)
