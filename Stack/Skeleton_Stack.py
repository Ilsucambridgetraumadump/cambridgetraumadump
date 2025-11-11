def push(new_item):
    global top, my_stack
    added = False
    if top == len(my_stack):
        print("stack is full")
    else:
        i = 0
        while i <= len(my_stack):
            if my_stack[i] != "":
                i = i + 1
            else:
                my_stack[i] = new_item
                added = True
    return added

    

def pop():
    pass

def traverse():
    pass

def search(search_item):
    pass





#******** Main module *************
my_stack = ["" for i in range(6)] # String 
top = -1 # Integer 
choice = ""
while choice != "5":
    print("1 to push ")
    print("2 to Pop")
    print("3 to Print All/Trasverse")
    print("4 Search")
    print("5 to quit ")
    choice = input("Select the menu option")
    if choice == "1":
        new_item = input("enter item to push")
        push(new_item)

    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    elif choice == "5":
        print("Good Bye....")

        
