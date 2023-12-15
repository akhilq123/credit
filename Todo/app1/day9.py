while True:
    command = input("Do you want to add,show,edit,complete or exit?")
    command_withoutspace=command.strip()


    if 'add' in command_withoutspace :
        # opening the file todoss.txt and saving the data inside to todos
        with open("file/todoss.txt", "r") as file :
            todos = file.readlines()
        # getting data from user and appending or adding it to todos
        todos.append(command_withoutspace[4:]+"\n")
        # reopening the file again in write mode and rewriting the entire file with the new todoss
        with open("file/todoss.txt", "w") as file:
            file.writelines(todos)

    elif 'show' in command_withoutspace:
        with open("file/todoss.txt", "r") as file:
            todos = file.readlines()
        for index,item in enumerate(todos):
            item = item.strip('\n')
            # removing the line break from the txt file so that we dont get 2 linebreaks
            print(f"{index+1}.{item.capitalize()}")
    #         we use capitalize function to get the first letter of the item capital for better reading
    elif 'edit' in command_withoutspace:
        number = int(command_withoutspace[5:])
        position = number -1

        with open("file/todoss.txt", "r") as file:
            todos = file.readlines()

        todos[position] = input("Enter new todo:")+"\n"

        with open("file/todoss.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in command_withoutspace :
        num = int(command_withoutspace[8:])

        with open("file/todoss.txt", "r") as file:
            todos = file.readlines()
        completed = todos[num-1].strip("\n")
        print(f"'{completed}' is marked as completed and is removed from to do list")
        todos.pop(num-1)
        with open("file/todoss.txt", "w") as file:
            file.writelines(todos)

    elif 'exit' in command_withoutspace:
        break
    else:
        print("Hey you entered a wrong command")
#         we can use any variable here as it will be defined on the go but to make debugging easy we use '_'
print("Bye")