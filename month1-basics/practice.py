name = input("What is your name? ")
age = int(input("What is your age? "))

print("Hello", name)

if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")