#Capstone_3_Task_manager\
The program helps progress tracking by means of managing tasks and users of an organisation.\
Program verifies the user and their password if it corresponds to the details of user.txt file. In order to determine the menu options available which are user specific.\
The admin gets six menu options available, admin is the only one that can Register new users, Generate reports and View statistics.\
Other users only have access to three options which they share with the admin being that it's Adding a task, View all task and View they own tasks.\
\
The program once logged in it display the menu for the specific user, if user selects Add Task, they should fill in the details required to add a task such the username to whom the task will be assigned to, title of the task, discription of task, due date of task, the date task is assigned and if the task has been complted or not. Then save the deetails to tasks.txt file.\
\
If user selects View all tasks, the program reads tasks.txt file and displays all tasks that have been assigned to the screen.\
\
If user selects View my tasks, the program reads tasks.txt file verifies if the logged in username has a task(s) assigned to them and displays them, if not available an message will notice the user.\
User is able to view a specific task individually to edit it if they select the option to view the specific task, then they will be required to enter the task number for the task they wish to edit, the task number and username is verified with tasks.txt file if correct then user is able to pick what they want to edit.\
If user wants to mark task as complete, change the due date or change username task was assigned to. Once done update the tasks.txt file. User also has the option to return to main menu.\
\
Since only the admin can register new user, when they select Register the username is verified that it's the admin that's chosen the option.\
Program will request new username and password and confirm the password before adding it to the user.txt file, if the user can't confirm their password the new user will not be added. But the program checks if the new user isn't already an existing user to avoid duplicating.\
\
The admin is the only one able to view the statistics, thus if they select display statistics, the username will be verified if it's the admin.\
Both task_overview.txt and user_overview.txt files will be read and the contents display on screen representing the statistics of the program.\
\
Lastly the since the admin is the only one with access to generate reports if they select Generate Report the program verifies if the admin is the one individual that is requesting access.\
Once access is granted the user.txt and tasks.txt file is read to count the number of users, count the number of tasks assigned to the admin, number of tasks completed by the admin, number of incomplete tasks assigned to the admin, counts the total number of completed tasks assigned to every user, counts the number of incomplete tasks assigned to every user, counts the number of overdue incomplete tasks as well as overdue incomplete tasks that were assigned to the admin.
Also the program should calculate the percentage of incomplete tasks, percentage of overdue tasks, percentage of tasks assigned to the admin, percentage of complete and incomplete tasks assigned to the admin and percentage of incomplete and overdue tasks the were assigned to the admin.\
Then write all these details calculated into the user_overview.txt file and task_overview.txt file as a report in a text file.\
\
To end the program the user can select exit.