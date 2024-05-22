def triangleTest(side1, side2, side3):
   
    sides = sorted([side1, side2, side3])
    return sides[0] + sides[1] > sides[2]


print(triangleTest(3, 4, 5)) 
print(triangleTest(1, 1, 2))  

def good_morning(name):
    print(f"Good morning, {name}!")

def good_afternoon(name):
    print(f"Good afternoon, {name}!")

def good_evening(name):
    print(f"Good evening, {name}!")

def greet_user():
    name = input("What's your name: ")
    time = input("What time is it (HH:MM): ")
    hour = int(time.split(":")[0])
    
    if 0 <= hour < 12:
        good_morning(name)
    elif 12 <= hour < 18:
        good_afternoon(name)
    elif 18 <= hour < 24:
        good_evening(name)
    else:
        print("Invalid time format")

greet_user()

def getEven(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


numsList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = getEven(numsList)
print(even_numbers) 
