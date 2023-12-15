# we seperate the functions from the module of the program, so we moved get_todo()
# and write_todo() to a python file 'functions' which is in the folder 'modules'
from modules import functions

while True:
    command = input("Do you want to add,show,edit,complete or exit?")
    command_withoutspace = command.strip()

    # .startswith() will check if the variable starts with the character given inside the ()
    if command_withoutspace.startswith('add'):
        # opening the file todoss.txt and saving the data inside to todos
        todos = functions.get_todo()
# here we are calling the 'get_todo()' from 'functions' file so we use file_name.function that is here functions.get_todo()
        # getting data from user and appending or adding it to todos
        todos.append(command_withoutspace[4:] + "\n")
        # reopening the file again in write mode and rewriting the entire file with the new todoss
        functions.write_todo(todos)

    elif command_withoutspace.startswith('show'):
        todos = functions.get_todo()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            # removing the line break from the txt file so that we don't get 2 linebreaks
            print(f"{index + 1}.{item.capitalize()}")
    #         we use capitalize function to get the first letter of the item capital for better reading
    elif command_withoutspace.startswith('edit'):
        try:
            number = int(command_withoutspace[5:])
            position = number - 1

            todos = functions.get_todo()

            todos[position] = input("Enter new todo:") + "\n"

            functions.write_todo(todos)
        except ValueError:
            print("Your command is not valid")
            # now we have to make the program start from  begining for this we can use continue which is the opposite
            # of break
            continue


    elif command_withoutspace.startswith('complete'):
        try:
            num = int(command_withoutspace[8:])

            todos = functions.get_todo()
            completed = todos[num - 1].strip("\n")
            print(f"'{completed}' is marked as completed and is removed from to do list")
            todos.pop(num - 1)
            functions.write_todo(todos)
        except IndexError:
            print("Your command is not valid valid range")
            continue
    elif 'exit' in command_withoutspace:
        break
    else:
        print("Hey you entered a wrong command")
#         we can use any variable here as it will be defined on the go but to make debugging easy we use '_'
print("Bye")
