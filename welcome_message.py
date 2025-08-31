name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello", name + "!")
print("Welcome to Python programming.")
print("You are", age, "years old.")
print("Next year, you will be", age + 1, "years old.")

if age < 18:
    print("Note: You are under 18, enjoy learning and have fun!")
else:
    print("Great! You are 18 or older, keep up the learning journey!")
