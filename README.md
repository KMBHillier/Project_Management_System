# Task Management System
This is a simple task management system that allows users to register, login, and add tasks. Only admin can register new users and the system only recognizes the correct credentials. The system also allows users to view all tasks and view their assigned tasks and can also generate a report on the tasks assigned to each user.

## Features
- User registration and login
- Adding tasks
- View all tasks
- View assigned tasks
- Generating user report

## How to Use
- Run the script in a Python environment
- The system will prompt for a username and password
- If you are an admin, you will be able to register new users and access the user report generation feature
- If you are a regular user, you will be able to add new tasks and view assigned tasks

## Dependencies
- tabulate
- datetime

## File Structure
- The script uses two text files user.txt and tasks.txt to store user information and task information respectively.
- user.txt stores the usernames and passwords of registered users.
- tasks.txt stores the tasks information like task number, assigned to, task title, task description, date assigned, due date, and task completion status.
- The script also generates a user_overview.txt file which contains user report

## Note
- Be sure that all the files are in the same directory as the script
- user_overview.txt will be overwritten every time the user report is generated
- The script uses the latest information available in the tasks.txt and user.txt files at the time of running the script, so be sure to keep them updated.

This script is useful for small teams to manage and keep track of their tasks and also to generate a report on how the tasks are assigned among the team.
