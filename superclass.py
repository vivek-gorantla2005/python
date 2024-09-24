class animal:
    def __init__(self) -> None:
        print("dheeraj is animal")

class dog(animal):
    def __init__(self) -> None:
        super(dog,self).__init__()
        print("dheeraj is a dog")
    
class bark(dog):
    def __init__(self) -> None:
        super(bark,self).__init__()
        print("dheeraj barks")
a = bark()