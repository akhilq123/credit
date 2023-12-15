todos= []

while True:
    command = input("Do ou want to add,show,edit,complete or exit?")
    command_withoutspace=command.strip()

    match command_withoutspace :
        case 'add' :
            # opening the file todoss.txt and saving the data inside to todos
            file = open("file/todoss.txt", "r")
            todos = file.readlines()
            file.close()
            # getting data from user and appending or adding it to todos
            todos.append(input("enter a todo")+"\n")
            # reopening the file again in write mode and rewriting the entire file with the new todoss
            file = open("file/todoss.txt", "w")
            file.writelines(todos)
            file.close()

        case 'show' :
            file = open("file/todoss.txt", "r")
            todos = file.readlines()
            file.close()
            for index,item in enumerate(todos):
                print(f"{index+1}.{item.capitalize()}")
        #         we use capitalize function to get the first letter of the item capital for better reading
        case 'edit' :
            number = int(input("Enter the number of to do to edit:"))
            position = number -1
            todos[position] = input("Enter new todo:")
        case'complete' :
            num = int(input("enter number of todo to complete: "))
            todos.pop(num-1)
        case 'exit' :
            break
        case _ :
            print("Hey you entered a wrong command")
#         we can use any variable here as it will be defined on the go but to make debugging easy we use '_'
print("Bye")
