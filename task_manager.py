from datetime import date
from datetime import datetime
import re

#registration function definition
def reg_user():
    register= True
    while register:
        #if user selects 'r' then they must enter a new username and password and confirm it before adding to user.txt
        new_username= input("Enter new username: ")
        new_password= input("Enter new password: ")
        confirm_password= input("Confirm password: ")

        #reads user file to verify if new user already exists.
        with open("user.txt",'r', encoding='utf-8') as user_file:
            user_list= user_file.readlines()
            not_duplicate= True #duplicate control veriable.

            for login_list in user_list:
                login= login_list.split(', ')
                #verifies duplication
                if(new_username== login[0]):
                    print("The user you are trying to add already exists, please add new user.")
                    not_duplicate= False
                    break

            #if user is actual a new user then it can proceed to add it to a file.
            if(not_duplicate== True):
                #confirm password and if it matches then add new user to user.txt
                if(new_password==confirm_password):
                    with open("user.txt",'a',encoding='utf-8') as user_file:

                        #add new user to user.txt
                        new_user= '\n'+new_username+', '+new_password
                        user_file.write(new_user)
                        print("Registration complete! \n")
                        register= False

                #error message if passwords don't match.    
                else:
                    print("\nInvalid, make sure password is the same.")

#function definition to add a task
def add_task():
    #adds a task number that the user can use to specifically get the task.
    with open("tasks.txt",'r',encoding='utf-8') as task_file:
        all_tasks= task_file.readlines()
        task_list= all_tasks[-1]
        tasks= task_list.split(', ')
        task_num= int(tasks[1])+1

    #ask user to complete the info needed to add a task.
        print("Enter the details required to add a task.")
        assigned_username= input("Username of person the task is assigned to: ")
        title_task= input("Title of the task: ")
        discription_task= input("Add the discription of the task: ")
        due_date= input("Due date of the task(e.g. 14 Jan 2010): ")
        date_assigned= date.today().strftime('%d %b %Y') #learned about the date method from stackoverflow to capture current date.
        task_complete= 'No'

        #add new task to tasks.txt file.
        with open("tasks.txt",'a',encoding='utf-8') as task_file:
            task_info= '\n'+assigned_username+', '+str(task_num)+', '+title_task+', '+discription_task+', '+due_date+', '+date_assigned+', '+task_complete
            task_file.write(task_info)

#function definition to view all tasks.
def view_all():
    #open tasks.txt
    with open("tasks.txt",'r',encoding='utf-8') as task_file:
        
        #reads file and displays all tasks.
        all_tasks= task_file.readlines()
        for task_list in all_tasks:
            tasks= task_list.split(', ')

            #displays every detail of the file in a readable format
            print('Assigned to: '+ tasks[0])
            print('Task number: ' +tasks[1])
            print('Title of task: '+ tasks[2])
            print('Task discription: '+ tasks[3])
            print('Due date: '+ tasks[4])
            print('Assigned date: '+ tasks[5])
            print('Completion: '+ tasks[6])

#function definiation to view user's tasks.
def view_mine(username):
    assigned= False #this is to verify if user has tasks.
    end_view= False
    while end_view== False: #loops through all the user's tasks, until they either choose to edit or go to main menu.
    
        task_view= input("\nEnter \'v\' to view all your tasks or \'s\' to view specific task: ").lower()
        if(task_view=='v'):
            #opens tasks.txt
            with open("tasks.txt",'r+',encoding='utf-8') as task_file:
                all_tasks= task_file.readlines()
            
                #checks if logged in uesrname matches the username in the tasks file.
                for task_row in all_tasks:
                    my_tasks= task_row.split(', ')
                    if(username== my_tasks[0]):

                        #displays every detail of the file in a readable format
                        print('\nAssigned to: '+ my_tasks[0])
                        print('Task number: '+ my_tasks[1])
                        print('Title of task: '+ my_tasks[2])
                        print('Task discription: '+ my_tasks[3])
                        print('Due date: '+ my_tasks[4])
                        print('Assigned date: '+ my_tasks[5])
                        print('Completion: '+ my_tasks[6])
                        assigned= True

                #if user doesn't have tasks assigned to them it will display message.
                if(assigned== False):
                    print("--No tasks assigned to you.--")
                    end_view= True    

        elif(task_view=='s'):
            with open("tasks.txt",'r+',encoding='utf-8') as task_file:
                all_tasks= task_file.readlines()
                #all_tasks_2= task_file.read()#####
                for task_row in all_tasks:
                    my_tasks= task_row.split(', ')
                    if(username== my_tasks[0]):
                        assigned= True
                        
            with open("tasks.txt",'r+',encoding='utf-8') as task_file:
                
                if(assigned== True): #this verifies if user has any tasks assigned to them.
                    #asks user for task number that will be used to edited. And '-1' to go back to main menu.
                    task_num= input("\nEnter task number to get specific task e.g 1000 (\'-1\' to go to main menu): ")
                    if(task_num != '-1'):
                        #checks if entered task number matches task number in file.
                        for task_row in all_tasks:
                            specific_task= task_row.split(', ')                            
                            
                            if(task_num== specific_task[1] and username== specific_task[0]): #verifies entered task number and the username are in the same row/line.

                                #ask user what they want to edit, m for complete task or e to edit the task.
                                edit_option= input("Enter \'m\' to mark task or \'e\' to edit task: ").lower()
                                if(edit_option=='m'):
                                    #this part of the task was unforgiving.
                                    incomplete_task= task_row #stores the unchaned task row in a variable so that it can be replaced with the new changed task row.
                                    complete_task= task_row.replace('No','Yes') #replaces 'No' with 'Yes' showing task is complete.

                                    all_tasks= task_file.read()
                                    task_file.seek(0) #places the curser at the begining of the file.
                                    task_file.write(re.sub(incomplete_task,complete_task, all_tasks)) #replace the old file with a new changed file
                                    print('Task mark updated!')

                                elif(edit_option=='e'):  
                                    
                                    #checks if task is completed because only the incomplete tasks can be edited.
                                    if(specific_task[6].strip('\n')=='No'):                                        
                                        #asks user what they want to edit username or due date, then verifies if they entered correctly.
                                        edit_choice= input("Enter \'u\' to edit the username or \'d\' to edit the due date: ").lower()
                                        if(edit_choice=='u'):
                                            edit_username= input("Add new username: ") 
                                            old_username= task_row #store old task row with old username that will be used in the substitution when writing to file.
                                            new_username= task_row.replace(specific_task[0],edit_username) #stores and replaces the old username in task row with a new username 

                                            all_tasks= task_file.read()
                                            task_file.seek(0) #set curser at the begining of file
                                            task_file.write(re.sub(old_username,new_username, all_tasks)) #overwrite the old file content with the new content with changes.
                                            print("Username updated!")

                                        elif(edit_choice=='d'):
                                            date_edit= True #error loop control variable 
                                            while date_edit:

                                                new_day_date= int(input("Add new Day date(e.g 25): "))
                                                if(new_day_date> 0 and new_day_date<= 31): #checks if day is within 1 and 31

                                                    new_month=input("Add new Month(e.g Feb): ").title()
                                                    new_month= new_month[0:3] #takes only 3 letters from the month even if user enters the full name of a month

                                                    new_year= int(input("Add new Year(e.g 2010): "))
                                                    if(new_year> 1000 and new_year<9999): #checks if user entered a real year

                                                        new_due_date= str(new_day_date)+' '+new_month+' '+str(new_year) #concatinates the entered new date.
                                                        old_date= task_row
                                                        new_date= task_row.replace(specific_task[4],new_due_date) #replaces the old date with new date.

                                                        all_tasks= task_file.read()
                                                        task_file.seek(0) #places curser at the begining of file.
                                                        task_file.write(re.sub(old_date, new_date, all_tasks)) #overwrites old date in file with a new date by replacing the the whole file.
                                                        
                                                        print("Due date updated!")
                                                        date_edit= False #set to false to end loop.
                                                    else:
                                                        print("Invalid year entered.")
                                                else:
                                                    print("Invalid day entered.")
                                                #read file again to make sure the date assigned doesn't change to current date.    
                                                all_tasks= task_file.read()
                                                task_file.seek(0) #places curser at the begining of file.

                                                #ensuring the date assigned doesn't change by writing the old date back to file.
                                                assigned_date= task_row.replace(specific_task[5],specific_task[5])
                                                task_file.write(re.sub(old_date, assigned_date, all_tasks))
                                                print('File updated!')

                                        else:
                                            print("Invalid entry. Make sure you entered \'u\' to edit the username or \'d\' to edit the due date.")
                                    else:
                                        print("Task already completed.")                                        
                                else:
                                    print("Invalid entry. Make sure you entered \'m\' to mark task or \'e\' to edit task.")

                            #else:
                                #print("The entered task number is invalid.")
                        
                    elif(task_num== '-1'):
                        end_view= True
                        break
                        
                #if user doesn't have tasks assigned to them it will display message.        
                if(assigned== False):
                    print("--No tasks assigned to you.--")
                    end_view= True         
                    
        else:
            print("Invalid entry, make sure you entered \'v\' to view all your tasks or \'s\' to view specific task.")

#function definition to view all statistics of tasks.
def display_stats():
    #open tasks.txt
    with open("task_overview.txt",'r+',encoding='utf-8') as task_overview_file:
        print("-----Task Overview-----")
        #reads tasks.txt file to count number of tasks.
        task_overview= task_overview_file.read()     
        print(task_overview)   
    
    #open users.txt
    with open("user_overview.txt",'r+',encoding='utf-8') as user_overview_file:
        print("-----User Overview-----")
        #reads user.txt file to count number of users.
        user_overview= user_overview_file.read()
        print(user_overview)

#function definition to generate task report and user report.
def generate_report(username):
    #task_overview.txt file
    with open("tasks.txt",'r+', encoding='utf-8') as task_file:
        all_tasks= task_file.readlines()
        #variable declaration
        num_tasks= 0
        num_tasks_assigned= 0
        completed_tasks= 0
        incomplete_tasks= 0
        overdue_incomplete_tasks= 0
        overdue_incomplete_assigned_tasks= 0
        completed_assigned_tasks= 0
        incomplete_assigned_tasks= 0

        for task_list in all_tasks:
            tasks= task_list.split(', ')
            num_tasks+= 1

            #counts number of tasks assigned to user
            if(username==tasks[0]):
                num_tasks_assigned+= 1
            
            #counts the number of completed assigned tasks. 
            if(username==tasks[0] and tasks[6].strip('\n')=='Yes'):
                completed_assigned_tasks+= 1

            #counts the number of incompleted assigned tasks.
            if(username==tasks[0] and tasks[6].strip('\n')=='No'):
                incomplete_assigned_tasks+= 1

            #counts number of completed tasks
            if(tasks[6].strip('\n')=='Yes'):
                completed_tasks+= 1
            #counts number of incompleted tasks
            if(tasks[6].strip('\n')=='No'):
                incomplete_tasks+= 1

            due_date= datetime.strptime(tasks[4], '%d %b %Y').date() #due date
            today = date.today() #today's date
            #compares the due date with today's date, if todays date is greater than the due date then it counts it.
            if(today> due_date and tasks[6].strip('\n')=='No'):
                overdue_incomplete_tasks+= 1
            
            #counts incomplete and overdue assigned tasks.
            if(username== tasks[0] and today> due_date and tasks[6].strip('\n')=='No'):
                overdue_incomplete_assigned_tasks+= 1
        
        #calculates the incomplete and overdue incomplete tasks percentage.
        incomplete_percentage= (incomplete_tasks/num_tasks)*100
        overdue_percentage= (overdue_incomplete_tasks/num_tasks)*100

        #calculates the percentage of num tasks assigned.
        assigned_task_percentage= (num_tasks_assigned/num_tasks)*100
        
        #calculates the percentage of completed assigned tasks. 
        completed_assigned_tasks_percentage= (completed_assigned_tasks/num_tasks_assigned)*100

        #calculates the percentage of incompleted assigned tasks.
        incomplete_assigned_tasks_percentage= (incomplete_assigned_tasks/num_tasks_assigned)#*100

        #calculates the percentage of incomplete and overdue assigned tasks.
        incomplete_overdue_assigned_tasks_percentage= (overdue_incomplete_assigned_tasks/num_tasks_assigned)*100

    with open("task_overview.txt",'w', encoding='utf-8') as task_overview_file:
        #overwrite/update the old file with new task overview  
        new_task_overview= "Number tasks: "+ str(num_tasks)+'\n'+ "Completed tasks: "+ str(completed_tasks)+'\n'+ "Incomplete tasks: "+ str(incomplete_tasks)+'\n'+ "Overdue imcomplete tasks: "+ str(overdue_incomplete_tasks)+'\n'+ "Incomplete task percentage: %"+ str(round(incomplete_percentage,2))+'\n'+ "Overdue task percentage: %"+ str(round(overdue_percentage,2))+'\n'
        task_overview_file.write(new_task_overview)
        print('Task overview updated!')

    with open("user.txt",'r+', encoding='utf-8') as user_file:
        #reads user file and counts the number of users registered.
        all_users= user_file.readlines()
        num_users= 0          
        #increment num users in the file being counted.
        for user_list in all_users:
            num_users+= 1
    
    with open("user_overview.txt",'w', encoding='utf-8') as user_overview_file:
        #overwrites/updates the old file with new user overview file.
        new_user_overview= 'Total number of users registered: ' +str(num_users)+'\n'+ 'Total number of tasks: ' +str(num_tasks)+'\n'+ 'Percentage of number of tasks assigned: %' +str(round(assigned_task_percentage))+'\n'+ 'Percentage of completed assigned tasks: %' +str(round(completed_assigned_tasks_percentage))+'\n'+ 'Percentage of incomplete assigned tasks: %' +str(round(incomplete_assigned_tasks_percentage))+'\n'+ 'Percentage of incomplete and overdue assigned tasks: %' +str(round(incomplete_overdue_assigned_tasks_percentage))+'\n'
        user_overview_file.write(new_user_overview)
        print('User overview updated!')

#login details.
print("Enter login details")
username= input("Usernmae: ")
password= input("Password: ")

#loop login verification until user enters valid login details.
access= True
while access:

    #read file to verfity login details.
    with open("user.txt",'r',encoding='utf-8') as user_file:

        #pass file content to a variable that will be used for verification.
        user_list= user_file.readlines()

        #loops through list to check if the entered username and password if it matches any saved usernames.
        for login_list in user_list:
            login= login_list.split(', ')

            #checks if both username and password are correct. 
            if(username== login[0] and password==login[1].replace('\n','')):
                print("Login successful!")
                access= False

        #error message if user enters the wrong login details.    
        if(access==True):
            print("Enter a valid username and password!")
            username= input("Usernmae: ")
            password= input("Password: ")

#loops through options until user exits program.
end= True #control variable if it's False it ends program.
while end:

    #checks if username is admin or not to determine which menu option to display.
    if(username=='admin'):
        #these are the admin's menu options.
        option= input("\nPlease select one of the following options: \nr- \tregister user \na- \tadd task \nva- \tview all tasks \nvm- \tview my tasks \ngr- \tgenerate reports \nds- \tdisplay statistics \ne- \texit \nEnter option: ").lower()  
    
    else:
        #these are the user's menu options.
        option= input("\nPlease select one of the following options: \na- \tadd task \nva- \tview all tasks \nvm- \tview my tasks \ne- \texit \nEnter option: ").lower()

    #if user selects 'e' it ends the program.
    if(option== 'e'):
        print("--------------------------Program Ended--------------------------")
        end= False

    #only the admin has access to register users. if admin selects 'r' it will allow them to add a new user.
    elif(option== 'r' and username== 'admin'):
        print("\n*****Registration*****\n")
        #call reg_user function to add new user
        reg_user()
        
    #if user selects 'a' then the program asks them to add a task.
    elif(option== 'a'):
        print("\n*****Add Task*****\n")
        #calls add_task function to add a task to it.
        add_task()

    #if user selects 'va' the program will display all the tasks.
    elif(option== 'va'):
        print("\n*****All Tasks*****\n")
        view_all()

    #if user selects 'vm' the program will only display their tasks.
    elif(option== 'vm'):
        print("\n*****Your Tasks*****")
        view_mine(username)
     
    #if user selects 'ds' the program reads through tasks file and user file to count and display the number of tasks and users.
    elif(option== 'ds' and username== 'admin'):
        print("\n*****Statistics*****\n")
        display_stats()
    
    #if user selects 'gr' the program generates a report.
    elif(option== 'gr' and username== 'admin'):
        print("\n*****Generate Report*****\n")
        generate_report(username)

    #error if user selects option that's not in the menu
    else:
        print("Invalid Entry!")