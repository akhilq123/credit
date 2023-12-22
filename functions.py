import json
import streamlit as st

destination_file = 'dictionary.txt'

def get_todo(filepath=destination_file):
    """
    Read a list file and return the items inside, default value of filepath is given,
    if accessing a different file you can give value in the function call
    """
    with open(filepath, "r") as files:
        local_todos = files.readlines()
    return local_todos


def write_todo(content,filepath=destination_file):
    with open(filepath, "w") as files:
        files.writelines(content)

def read_json(filepath=destination_file):
    with open(filepath) as file:  # Reading the file here
        data = json.load(file)
    return data


def write_json(content,filepath=destination_file):
    with open(filepath, 'w') as file:  # Writing to file here
        file.write(json.dumps(content))
def confirm():
    local = st.button("SAVE")
    return local

def confirm_income(parent,child,new):
    local = st.button("SAVE")
    if local:
        data = read_json()
        data[parent][child]-= new
        write_json(data)
        st.write("Balance Updated")

def confirm_expense(parent,child,new):
    local = st.button("SAVE")
    if local:
        data = read_json()
        data[parent][child]+= new
        write_json(data)
        st.write("Balance Updated")
def confirm_add(parent,child,new):
    local = st.button("SAVE")
    if local:
        data = read_json()
        data[parent][child] = new
        write_json(data)
        st.write("Balance Updated")


def income(value):
    loc = st.toggle("LOC")
    card = st.toggle("card", disabled=loc)
    if loc:
        option = st.selectbox(
            "Choose",
            ("scotia_loc", "rbc_loc"),
            index=None,
            placeholder="Select LOC to edit",
        )
        if option == "scotia_loc":
             confirm_income("loc",option,value)
        elif option == "rbc_loc":
             confirm_income("loc",option,value)
    elif card:
        option = st.selectbox(
            "Choose card to update",
            ("simplii", "tangerine", "bmo", "mbna", "rbc"),
            index=None,
            placeholder="Select card to edit",
        )
        match option:
            case "simplii":
                 confirm_income("card",option,value)
            case "tangerine":
                 confirm_income("card",option,value)
            case "bmo":
                 confirm_income("card",option,value)
            case "mbna":
                if confirm():
                     confirm_income("card", option, value)
            case "rbc":
                 confirm_income("card",option,value)

def expense(value):
    loc = st.toggle("LOC")
    card = st.toggle("card", disabled=loc)
    if loc:
        option = st.selectbox(
            "Choose",
            ("scotia_loc", "rbc_loc"),
            index=None,
            placeholder="Select LOC to edit",
        )
        if option == "scotia_loc":
            confirm_expense("loc",option,value)
        elif option == "rbc_loc":
            confirm_expense("loc",option,value)
    elif card:
        option = st.selectbox(
            "Choose card to update",
            ("simplii", "tangerine", "bmo", "mbna", "rbc"),
            index=None,
            placeholder="Select card to edit",
        )
        match option:
            case "simplii":
                confirm_expense("card",option,value)
            case "tangerine":
                confirm_expense("card",option,value)
            case "bmo":
                confirm_expense("card",option,value)
            case "mbna":
                confirm_expense("card",option,value)
            case "rbc":
                confirm_expense("card",option,value)
def add(value=0,task="edit"):
    if task=="edit":
        new = st.number_input("Enter updated value")
        loc = st.toggle("LOC",key="loc")
        card = st.toggle("card", disabled=loc)
        if loc:
            option = st.selectbox(
                "Choose",
                ("scotia_loc", "rbc_loc"),
                index=None,
                placeholder="Select LOC to edit",
            )
            if option == "scotia_loc":
                confirm_add("loc",option,new)
            elif option == "rbc_loc":
                confirm_add("loc",option,new)
        elif card:
            option = st.selectbox(
                "Choose card to update",
                ("simplii", "tangerine", "bmo", "mbna", "rbc"),
                index=None,
                placeholder="Select card to edit",
            )
            match option:
                case "simplii":
                    confirm_add("card", option, new)
                case "tangerine":
                    confirm_add("card", option, new)
                case "bmo":
                    confirm_add("card", option, new)
                case "mbna":
                    confirm_add("card", option, new)
                case "rbc":
                    confirm_add("card", option, new)

    elif task=="income":
        income(value)
    elif task=="expense":
        expense(value)

def balance():
    bal = st.checkbox("SHOW BALANCE")
    data = read_json()
    if bal:
        x = 0
        y = 0
        for i, j in data["loc"].items():
            y += j
            st.write(i, ":", j)
        for i, j in data["card"].items():
            x += j
            st.write(i, ":", j)
        st.write("Total LOC:", y)
        st.write('Total Card:', x)
        st.write("Total Debt =", x + y)
        if confirm():
            data = read_json()
            data["total"]["card_total"] = x
            data["total"]["loc_total"] = y
            data["total"]["total"] = data["total"]["card_total"] + data["total"]["loc_total"]
            write_json(data)
            st.write("Balance Updated")


# '__name__' is a variable that python creates, if the code is run directly the variable will have value '__main__'
# if the code is called by importing in other file '__name__' will have some other value
#  so the if statement below will only be executed if we run the file here, it wont execute in any other files
if __name__ =="__main__" :
    print("hello")
    print(get_todo())