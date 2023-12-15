todos= []

while True:
    command = input("Do ou want to add,show,edit or exit?")
    command_withoutspace=command.strip()

    match command_withoutspace :
        case 'add' :
            todos.append(input("enter a todo"))
        case 'show' :
            for item in todos:
                print(item.capitalize())
        #         we use capitalize function to get the first letter of the item capital for better reading
        case 'edit' :
            number = int(input("Enter the number of to do to edit:"))
            position = number -1
            todos[position] = input("Enter new todo:")
        case 'exit' :
            break
        case _ :
            print("Hey you entered a wrong command")
#         we can use any variable here as it will be defined on the go but to make debugging easy we use '_'
print("Bye")

# bonus to replace a string in list
cinemas = ["wolf of wallstreet","DC","marvel"]
for movie in cinemas :
    cinemas_without_space= movie.replace(' ','_')
    print(cinemas_without_space)

# tuples are same like list but not editable eg in this case would be :cinemas = ("wolf of wallstreet","DC","marvel")