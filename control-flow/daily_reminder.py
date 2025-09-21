# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Loop to validate priority input
priority = ""
while priority not in ("high", "medium", "low"):
    priority = input("Priority (high/medium/low): ")

# Loop to validate time-bound input
time_bound = ""
while time_bound.lower() not in ("yes", "no"):
    time_bound = input("Is it time-bound? (yes/no): ")

# Match-case statement to react based on priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an undefined priority"

# If statement to modify the reminder if the task is time-bound
if time_bound.lower() == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", message)
