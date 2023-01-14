import tabulate
import datetime
from datetime import date
# create a dictionary to hold the usernames and passwords
userbase = {}

# open the user text file and read each line, separating the words and removing \n from the end of each line
# then adding the usernames and passwords to userbase
# only recognises the correct credentials
with open("user.txt", "r+") as f:
    for line in f.readlines():
        username, password = line.split(",")
        userbase[username.strip()] = password.strip()

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in userbase and userbase[username] == password:
        print("Welcome!")
        break
    else:
        print("""The username or password you have entered is incorrect.
Please try again.""")



contents = ""
# only admin can register users
# admin also gets a statistics option in the menu


def reg_user():
    while True:
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm new password: ")
        error = 0

        if new_password == "":
            error = "Nice try, smartypants!"
        # check if the username is already in the dictionary
        if new_username in userbase:
            error = "The username you entered has already been used. Please enter a new username."

        if error == 0:
            if new_password == confirm_password:
                # add the new username and password to the dictionary
                userbase[new_username] = new_password
                # write the new username and password to the text file
                with open("user.txt", "a") as f:
                    f.write(f"\n{new_username}, {new_password}")
                print("New user registration successful!")
                break
            else:
                print("Your passwords don't match. Please try again")
                continue
        else:
            print(error)


def add_task():
    task_number = int(input("What number task is this: "))
    assigned = input("Who is this task assigned to: ")
    task_title = input("What is this task called: ")
    task_description = input("Describe the task: ")
    task_date = input("When is this task due: (YYYY-MM-DD) ")
    today = date.today()
    completion = "No"
    with open("tasks.txt", "a") as f:
        f.write(f"\n{task_number}, {assigned}, {task_title}, {task_description}, {today}, {task_date}, {completion},")
    print("Task added")


def view_all():
    with open("tasks.txt", "r") as f:
        tasks = []
        for line in f.readlines():
            contents = line
            contents_split = contents.split(",")

            # Add the task information to a list
            tasks.append([contents_split[0], contents_split[2], contents_split[1], contents_split[4], contents_split[5], contents_split[6], contents_split[3]])

        # Use the tabulate function to format the task information into a table
        print(tabulate.tabulate(tasks, headers=["Task Number", "Task", "Assigned to", "Date assigned", "Due Date", "Task Complete", "Task Description"]))


def view_mine():
    with open("tasks.txt", "r") as f:
        tasks = []
        for line in f.readlines():
            contents = line
            contents_split = contents.split(",")

            # Only add tasks that are assigned to the current user to the list
            if contents_split[1] == " " + username:
                tasks.append([contents_split[0], contents_split[2], contents_split[1], contents_split[4], contents_split[5], contents_split[6], contents_split[3]])
                # print the data in a table for easy reading
        print(tabulate.tabulate(tasks, headers=["Task Number", "Task", "Assigned to", "Date assigned", "Due Date", "Task Complete", "Task Description"]))
        # Allow the user to select a task or return to the main menu
        # Allow the user to select a task or return to the main menu
        while True:
            task_number = input("Enter the task number you want to view or -1 to return to the main menu: ")

            # If the user entered -1, return to the main menu
            if task_number == "-1":
                break

            # Check if the task exists and display it
            task_exists = False
            for task in tasks:
                if task[0] == task_number:
                    task_exists = True
                    print(f"Task: {task[1]}")
                    print(f"Assigned to: {task[2]}")
                    print(f"Date assigned: {task[3]}")
                    print(f"Due date: {task[4]}")
                    print(f"Task complete: {task[5]}")
                    print(f"Task description: {task[6]}")

            # If the task does not exist, print an error message
            if not task_exists:
                print(f"Task {task_number} does not exist.")
                break

            # Display the menu for task options
            print("1. Mark task as complete")
            print("2. Edit task")
            print("-1. Return to main menu")

            # Get the user's selection
            selection = input("What would you like to do with this task: ")

            # Handle the user's selection
            if selection == "1":
                # Mark the task as complete
                # Update the yes/no value in the list of tasks
                # Read in the contents of the tasks.txt file and store it in a list of lines
                with open("tasks.txt", "r") as f:
                    lines = f.readlines()

                # Iterate through the list of tasks
                for task in tasks:
                    # If the task has the specified task number, update its line in the list of lines
                    if task[0] == task_number:
                        task_line = f"{task[0]},{task[2]},{task[1]},{task[6]},{task[3]},{task[4]}, Yes\n"
                        task_index = int(task[0])-1
                        lines[task_index] = task_line

                # Write the updated list of lines back to the tasks.txt file
                with open("tasks.txt", "w") as f:
                    f.writelines(lines)
                print("Task marked as complete.")


            elif selection == "2":
                # Allow the user to edit the task
                # Check if the task has been completed
                if task[5] == " Yes" or task [5] == " Yes\n":
                    print("Task cannot be edited because it has already been completed.")
                else:
                    # Prompt the user for the new username and due date
                    new_username = input("Enter the new username for the task: ")
                    new_due_date = input("Enter the new due date for the task: ")

                    # Update the task with the new username and due date
                    with open("tasks.txt", "r") as f:
                        data = f.read()
                        for task in tasks:
                            if task[0] == task_number:
                                data = data.replace(task[1], new_username)
                                data = data.replace(task[4], new_due_date)
                                with open("tasks.txt", "w") as f:
                                    f.write(data)
                                print("Task edited.")
            elif selection == "-1":
                # Return to the main menu
                break
            else:
                # Handle invalid input
                print("Invalid selection. Please try again.")
                break


def display_statistics():
    print("\033[1m\033[4mTask Overview\033[0m\n")

    # try to open task_overview.txt in read mode
    try:
        with open('task_overview.txt', 'r') as f:
            # read all lines from the file
            lines = f.readlines()

        # print each line
        for line in lines:
            print(line)
    except FileNotFoundError:
        # if the file doesn't exist, run generate_user_file()
        generate_task_report()
        # then try to open the file again
        try:
            with open('task_overview.txt', 'r') as f:
                # read all lines from the file
                lines = f.readlines()
            # print each line
            for line in lines:
                print(line)
        except:
            print("Could not generate or open task_overview.txt")
    except Exception as e:
        # handle other exceptions
        print(f"An error occurred: {e}")

    print("\033[1m\033[4mUser overview\033[0m\n")

    # try to open user_overview.txt in read mode
    try:
        with open('user_overview.txt', 'r') as f:
            # read all lines from the file
            lines = f.readlines()

        # print each line
        for line in lines:
            print(line)
    except FileNotFoundError:
        # if the file doesn't exist, run generate_user_file()
        generate_user_report()
        # then try to open the file again
        try:
            with open('user_overview.txt', 'r') as f:
                # read all lines from the file
                lines = f.readlines()
            # print each line
            for line in lines:
                print(line)
        except:
            print("Could not generate or open user_overview.txt")
    except Exception as e:
        # handle other exceptions
        print(f"An error occurred: {e}")


def generate_task_report():
    with open('tasks.txt', 'r') as f:
        tasks = []
        for line in f.readlines():
            contents = line
            contents_split = contents.split(",")
            tasks.append([contents_split[0], contents_split[2], contents_split[1], contents_split[4], contents_split[5], contents_split[6], contents_split[3]])
    # count the total number of tasks
    total_tasks = len(tasks)

    # count the number of completed tasks
    completed_tasks = 0
    for task in tasks:
        if task[5] == " Yes\n":
            completed_tasks += 1


    # count the number of uncompleted tasks
    uncompleted_tasks = total_tasks - completed_tasks

    # count the number of tasks that are both incomplete and overdue

    overdue_incomplete_tasks = 0
    for task in tasks:
        # check if the task is incomplete
        if task[5] == " No\n":  # check if the task is incomplete
            # check if the due date has passed
            date_split = task[4].split("-")
            due_date = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
            if due_date < datetime.date.today():
                overdue_incomplete_tasks += 1

    # calculate the percentage of tasks that are incomplete
    incomplete_percentage = uncompleted_tasks / total_tasks
    incomplete_percentage_formatted = '{:.2%}'.format(incomplete_percentage)

    # calculate the percentage of tasks that are overdue
    overdue_percentage = overdue_incomplete_tasks / total_tasks
    overdue_percentage_formatted =  '{:.2%}'.format(overdue_percentage)

    # write the task overview to the task_overview.txt file
    with open("task_overview.txt", "w") as f:
        f.write(f"Total number of tasks: {total_tasks}\n")
        f.write(f"Number of completed tasks: {completed_tasks}\n")
        f.write(f"Number of incomplete tasks: {uncompleted_tasks}\n")
        f.write(f"Number of tasks incomplete and overdue: {overdue_incomplete_tasks}\n")
        f.write(f"Percentage of tasks incomplete: {incomplete_percentage_formatted}%\n")
        f.write(f"Percentage of tasks overdue: {overdue_percentage_formatted}%\n")
    print("A task report has been generated.")


def generate_user_report():
    with open("user_overview.txt", "w") as h:
        # count the number of tasks in tasks.txt
        global username
        with open("tasks.txt", "r") as f:
            tasks = []
            for line in f.readlines():
                contents = line
                contents_split = contents.split(",")
                tasks.append([contents_split[0], contents_split[2], contents_split[1], contents_split[4], contents_split[5],
                              contents_split[6], contents_split[3]])
            number_of_tasks = len(tasks)
            h.write(f"Total number of tasks: {number_of_tasks}\n")
        # create a dictionary to store the data for each user
        user_data = []

        # populate the list with the data for each user
        with open("user.txt", "r") as g:
            for line in g.read().split("\n"):
                contents = line
                contents_split = contents.split(",")
                user_data.append([contents_split[0], {"Total tasks": 0, "% of Total tasks": 0, "% of Tasks completed": 0,
                                                      "% of Tasks incomplete": 0, "% of Tasks incomplete and overdue": 0}])
                number_of_users = len(user_data)
        h.write(f"Number of users registered: {number_of_users}\n")
        # add the user to the list if they don't already exist
        found = False
        for user in user_data:
            if user[0] == username:
                found = True
                break
        if not found:
            user_data.append(
                [username, {"total_tasks": 0, "completed_tasks": 0, "incomplete_tasks": 0, "overdue_incomplete_tasks": 0}])

        # increment the appropriate task counter for the user
        for user in user_data:
            # get the username for the current user
            username = user[0]
            # reset the total tasks counter for the user
            total_tasks = 0
            # iterate over the tasks and check if the username is assigned to the task
            for task in tasks:
                if " " + username == task[2]:
                    total_tasks += 1
            # update the total tasks counter for the user in the user data
            user[1]["total_tasks"] = total_tasks

            # also find the percentage of total tasks assigned, but only if there are assigned tasks
            if total_tasks > 0:
                total_tasks_percentage = total_tasks / number_of_tasks
                total_tasks_percentage_formatted = '{:.2%}'.format(total_tasks_percentage)
            else:
                total_tasks_percentage_formatted = 0

            h.write(f"Total number of tasks assigned to {username}: {total_tasks}\n")
            h.write(f"Percentage of total tasks assigned to {username}: {total_tasks_percentage_formatted}%\n")


            # get the username for the current user
            username = user[0]
            # reset the completed tasks counter for the user
            completed_tasks = 0
            # iterate over the tasks and check if the username is assigned to the task and the task is marked as completed
            for task in tasks:
                if " " + username == task[2] and task[5] == " Yes\n":
                    completed_tasks += 1
            # turn the number into a percentage, but only if there are assigned tasks
            if total_tasks > 0:
                completed_tasks_percentage = completed_tasks / total_tasks
                completed_tasks_percentage_formatted = '{:.2%}'.format(completed_tasks_percentage)
            else:
                completed_tasks_percentage_formatted = 0
            # update the completed tasks counter for the user in the user data
            user[1]['completed_tasks'] = completed_tasks_percentage_formatted

            h.write(f"Percentage of completed tasks assigned to {username}: {completed_tasks_percentage_formatted}%\n")


            # get the username for the current user
            username = user[0]
            # reset the completed tasks counter for the user
            incomplete_tasks = 0
            incomplete_overdue_tasks = 0
            # iterate over the tasks and check if the username is assigned to the task and the task is marked as completed
            for task in tasks:
                if " " + username == task[2] and task[5] == " No\n":
                    incomplete_tasks += 1
                    date_split = task[4].split("-")
                    due_date = datetime.date(int(date_split[0]), int(date_split[1]), int(date_split[2]))
                    if due_date < datetime.date.today():
                        incomplete_overdue_tasks += 1
            # turn the numbers into a percentage, but only if there are assigned tasks
            if total_tasks > 0:
                incomplete_tasks_percentage = incomplete_tasks / total_tasks
                incomplete_tasks_percentage_formatted = '{:.2%}'.format(incomplete_tasks_percentage)
            else:
                incomplete_tasks_percentage_formatted = 0
            # update the completed tasks counter for the user in the user data
            user[1]['incomplete_tasks'] = incomplete_tasks_percentage_formatted
            if total_tasks > 0:
                incomplete_overdue_tasks_percentage = incomplete_overdue_tasks / total_tasks
                incomplete_overdue_tasks_percentage_formatted = '{:.2%}'.format(incomplete_overdue_tasks_percentage)
            else:
                incomplete_overdue_tasks_percentage_formatted = 0

            h.write(f"Percentage of incomplete tasks assigned to {username}: {incomplete_tasks_percentage_formatted}%\n")
            h.write(f"Percentage of incomplete and overdue tasks assigned to {username}: {incomplete_overdue_tasks_percentage_formatted}%\n")
    print("A user report has been generated")


if username == "admin":
    while True:
        # Print the menu
        print("Register new user - r")
        print("Add task - a")
        print("View all Tasks - va")
        print("View My tasks - vm")
        print("Display Statistics - ds")
        print("Generate task report - gtr")
        print("Generate user report - gur")
        print("Exit - e")

        # Prompt the user to choose an option
        option = input("Please select one of the above options: ").lower()

        if option == "r":
            # register new user
            reg_user()
        elif option == "a":
            # add a new task
            add_task()
        elif option == "va":
            # view all tasks listed
            view_all()
        elif option == "vm":
            # view all tasks listed under logged in user
            view_mine()
        elif option == "ds":
            # display statistics
            display_statistics()
        elif option == "gtr":
            # generate task reports
            generate_task_report()
        elif option == "gur":
            # generate user reports
            generate_user_report()
        elif option == "e":
            # Exit the program
            break
        else:
            print("Invalid option. Please try again.")

else:
    while True:
        # Print the menu
        print("Add task - a")
        print("View all Tasks - va")
        print("View My tasks - vm")
        print("Exit - e")

        # Prompt the user to choose an option
        option = input("Please select one of the above options: ").lower()

        if option == "a":
            # add a new task
            add_task()
        elif option == "va":
            # view all tasks listed
            view_all()
        elif option == "vm":
            # view all tasks listed under logged in user
            view_mine()
        elif option == "e":
            # Exit the program
            break
        else:
            print("Invalid option. Please try again.")