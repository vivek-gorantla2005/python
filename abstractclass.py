from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def size(self,name):
        pass

class rectangle(Shape):
    def size(self,name):
        print(f"this is a rectangle of name {name}")
        
r = rectangle()
r.size("rec")
