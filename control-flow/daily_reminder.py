# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"

# Modify the message if the task is time-bound
if time_bound.lower() == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print("Reminder:", message)
