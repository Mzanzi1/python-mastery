# Week 1 – Lesson 3

name = input("What is your name? ")
sessions = int(input("How many study sessions do you want?"))

print("Hello", name)
print("Let's count your study sessions.")

for i in range(sessions):
    print("Study session", i + 1)