from typing import Optional
class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional["Node"] = None

HEAD = None

def insert_beginning(data):
    global HEAD
    newnode = Node(data)
    
    if HEAD == None:
        HEAD = newnode
        return
    
    newnode.next = HEAD
    HEAD = newnode
    return

def insert_end(data):
    global HEAD
    newnode = Node(data)
    
    if HEAD is None:
        insert_beginning(data)
        return
    
    temp = HEAD
    while temp.next is not None:
        temp = temp.next
        
    temp.next = newnode
    return

def traverse():
    global HEAD
    
    if HEAD is None:
        print("List is empty")
        return
    
    temp = HEAD
    while temp is not None:
        print(temp.data, "->", end=" ")
        temp = temp.next
    
    print("\nend")
    return

def delete_beginning():
    global HEAD
    
    if HEAD is None:
        return
    
    HEAD = HEAD.next
    return

def delete_end():
    global HEAD
    
    if HEAD is None:
        return
    
    if HEAD.next is None:
        HEAD = None
        return
    
    temp = HEAD
    while temp.next.next is not None:
        temp = temp.next
        
    temp.next = None
    return 


while True:
    print("""
    1. Insert at beginning
    2. Insert at end
    3. Traverse
    4. Delete beginning
    5. Delete end
    6. Exit
    """)
    choice = int(input("Enter your choice: "))

    if choice == 1:
        n = int(input("Enter the number: "))
        insert_beginning(n)

    elif choice == 2:
        n = int(input("Enter the number: "))
        insert_end(n)

    elif choice == 3:
        traverse()

    elif choice == 4:
        delete_beginning()

    elif choice == 5:
        delete_end()

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")