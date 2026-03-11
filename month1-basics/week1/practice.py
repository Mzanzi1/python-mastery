name = input("What is your name? ")
sessions = int(input("How many study sessions do you want? "))

print("Hello", name)

for i in range(sessions):
    print("Study session", i + 1)

print("You completed", sessions, "study sessions.")