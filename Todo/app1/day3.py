todos = []

while True:
    command = input("Do ou want to add,show or exit?")
    command_withoutspace=command.strip()

    match command_withoutspace :
        case 'add' :
            todos.append(input("enter a todo: "))
        case 'show' :
            for item in todos:
                print(item.capitalize())
        #         we use capitalize function to get the first letter of the item capital for better reading
        case 'exit' :
            break
        case _ :
            print("Hey you entered a wrong command")
#         we can use any variable here as it will be defined on the go but to make debugging easy we use '_'
print("Bye")

# bonus

for x in 'itemssss':
    print(x.capitalize())
    # this will capitalize the individual alphabets in the string provided ie 'itemssss' 