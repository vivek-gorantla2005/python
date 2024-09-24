class rectangle:
    def __init__(self,lenght,breadth) -> None:
        self.lenght=lenght
        self.breadth = breadth
    def area(self):
        return self.lenght*self.breadth
    @classmethod
    def square(cls,side):
        return cls(side,side)

s=rectangle.square(10)
print("area is",s.area())
      