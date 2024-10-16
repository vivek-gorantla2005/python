arr = [1,2,3]
string = "vivek"
try:
    print(arr[2]) 
    
    # div = arr[1]/0
    # print(div)
    
    string = int(string)
    print(string)
    
except IndexError as e:
    print(f"error occoured : {e}")
except ZeroDivisionError as e:
    print(f"error occured : {e}")
except ValueError as e:
    print(f"value error occured : {e}")



try:
    f = open("hello.txt","r")
    print(f.content)
except FileNotFoundError as e:
    print(f"error occured : {e} ")



class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""
    pass
age = int(input("Enter your age: "))
try:
    if age <= 0 or age >= 100:
        raise InvalidAgeError("Please enter a valid age between 1 and 99.")
    else:
        print("Valid age")
        
except InvalidAgeError as e:
    print(e)
except ValueError as e:
    print(f"Error: {e}")
