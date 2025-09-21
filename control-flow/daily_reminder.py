# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")

# Prompt for priority with validation loop
priority = ""
while priority not in ("high", "medium", "low"):
    priority = input("Priority (high/medium/low): ")

# Prompt for time-bound with validation loop
time_bound = ""
while time_bound.lower() not in ("yes", "no"):
    time_bound = input("Is it time-bound? (yes/no): ")

# Process task based on priority using if-elif-else (match-case alternative)
if priority == "high":
    message = f"'{task}' is a high priority task"
elif priority == "medium":
    message = f"'{task}' is a medium priority task"
else:  # low
    message = f"'{task}' is a low priority task"

# Modify the reminder if the task is time-bound
if time_bound.lower() == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# Print the customized reminder
print("Reminder:", message)
