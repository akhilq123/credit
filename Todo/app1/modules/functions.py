def get_todo(filepath="file/todoss.txt"):
    """
    Read a list file and return the items inside, default value of filepath is given,
    if accessing a different file you can give value in the function call
    """
    with open(filepath, "r") as files:
        local_todos = files.readlines()
    return local_todos


def write_todo(content,filepath="file/todoss.txt"):
    """ write a to-do item in the text file.
    Default value of filepath is given,if accessing a different file you can give value in the function call
    or just give an argument for content only """
    with open(filepath, "w") as files:
        files.writelines(content)

# '__name__' is a variable that python creates, if the code is run directly the variable will have value '__main__'
# if the code is called by importing in other file '__name__' will have some other value
#  so the if statement below will only be executed if we run the file here, it wont execute in any other files
if __name__ =="__main__" :
    print("hello")
    print(get_todo())