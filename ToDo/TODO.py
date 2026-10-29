import os 
import json
TASKS_FILE ="tasks.json"
if os.path.exists(TASKS_FILE):
    with open(TASKS_FILE,"r") as f:
        tasks=json.load(f)
    else:
        tasks{}
i = 1
tasks = {}
while i != 0:
    print("""
Welcome to do list:
    1 Add a task
    2 Delete a task
    3 Update a task
    4 View tasks
    5 See tasks
""")
    i = int(input("Enter your choice : "))

    if i == 1:
        print("You are in Add a task function")
        task = input("Enter the task name : ")
        time_val = int(input("Enter the time : "))
        duration = input("Enter the duration of task : ")
        tasks[task] = {"time": time_val, "duration": duration}
        print("Task added successfully")
        i = int(input("Enter zero if you want to exit : "))

    elif i == 2:
        print("You are in Delete a task function")
        task = input("Enter the task name : ")
        if task in tasks:
            del tasks[task]
            print("Task deleted successfully")
        else:
            print("Task not found")
        i = int(input("Enter zero if you want to exit : "))

    elif i == 3:
        print("You are in Update a task function")
        task = input("Enter the task name : ")
        if task in tasks:
            print("What do you want to update?")
            print("1 Time")
            print("2 Duration")
            print("3 Both")
            choice = int(input("Enter your choice : "))
            if choice == 1:
                new_time = int(input("Enter new time : "))
                tasks[task]["time"] = new_time
                print("Time updated successfully")
            elif choice == 2:
                new_duration = input("Enter new duration : ")
                tasks[task]["duration"] = new_duration
                print("Duration updated successfully")
            elif choice == 3:
                new_time = int(input("Enter new time : "))
                new_duration = input("Enter new duration : ")
                tasks[task]["time"] = new_time
                tasks[task]["duration"] = new_duration
                print("Time and Duration updated successfully")
            else:
                print("Invalid choice")
        else:
            print("Task not found")
        i = int(input("Enter zero if you want to exit : "))

    elif i == 4:
        print("You are in View tasks function")
        if tasks:
            for task, details in tasks.items():
                print(f"Task: {task}, Time: {details['time']}, Duration: {details['duration']}")
        else:
            print("No tasks available")
        i = int(input("Enter zero if you want to exit : "))

    elif i == 5:
        print("You are in See tasks function")
        if tasks:
            for task, details in tasks.items():
                print(f"Task: {task}, Time: {details['time']}, Duration: {details['duration']}")
        else:
            print("No tasks available")
        i = int(input("Enter zero if you want to exit : "))

    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)
        print(f"Tasks saved to {TASKS_FILE}")