# Week 1 – Mini Program

print("Weekly Study Analyzer")

total_hours = 0

for i in range(7):
    hours = float(input(f"Enter study hours for day {i + 1}: "))
    total_hours = total_hours + hours

average = total_hours / 7

print("Total hours studied:", total_hours)
print("Average hours per day:", average)