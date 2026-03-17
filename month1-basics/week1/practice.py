# Week 2 – Lesson 1

print("Weekly Study Analyzer (List Version)")

hours_list = []

for i in range(7):
    hours = float(input(f"Enter study hours for day {i + 1}: "))
    hours_list.append(hours)

total_hours = sum(hours_list)
average = total_hours / len(hours_list)

print("Total hours studied:", total_hours)
print("Average hours per day:", round(average, 2))
print("Daily entries:", hours_list)