# 2. Daily to do list

to_do_list = []
index = +1



def add_item(to_do_list):
    number_item = int(input("How many tasks would you like to add to your list: \n" ))    
    for i in range(number_item):    
        list = input("Enter the task: \n").lower()
        date = input("When should this task be completed: \n")
        priority = input("What is the priority level: (High, Normal, Low) \n").capitalize()
        if list not in to_do_list:
            full_task = list + ":"+" "+"Complete by:"+" "+date +" "+"Priority:"+" "+priority
            to_do_list.append(full_task)
        else:
            print(list, "is in your list already.")
    print(to_do_list)
    
def show_item(to_do_list):
    print("\nTasks:")
    for count, lists in enumerate(to_do_list, start=1):

        if len(to_do_list) == 0:
            print("You currently have nothing to do. ")
        else: 
            print(count,".", lists)
             
def mark_item(to_do_list):
    mark_task = input("What task have you completed? ").lower()
    found = False
    for i in range(len(to_do_list)):
        if to_do_list[i].startswith(mark_task):
            to_do_list[i] += " (Completed)"
            found = True
            print(f"{mark_task} marked as completed.")
            break
    
    if not found:
        print(f"{mark_task} is not in your list.")

def remove_item(to_do_list):
    try:
        item = input("Which item would you like to remove from your list? ").lower()
        found = False
        for task in to_do_list:
            if item in task.lower(): 
                to_do_list.remove(task)
                found = True
                print(f"{task} was removed from your list.")
                break
        
        if not found:
            print(f"{item} is not in your list.")
    
    except ValueError:
        print("Error occurred while removing the item.")
  
def main(to_do_list):
    a = ''' 
    Hello, Welcome to your To Do List what would you like to do:
    '''   
    b = '''   
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
    '''
    print(a)
    print(b)
    print("**************************************")

    while True:
            user = input("What would you like to do?  \n")
            if user == "1":
                add_item(to_do_list)
                print(b)   
            elif user == "2":
                show_item(to_do_list)
                print(b)
            elif user == "3":
                mark_item(to_do_list)
                print(b)
            elif user == "4":
                remove_item(to_do_list)
                print(b)
            elif user =="5":
                print("Hope you have a great prductive day, good bye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        
       
        
main(to_do_list)