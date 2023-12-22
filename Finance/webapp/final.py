import streamlit as st
import json

destination_file = 'dictionary.txt'

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
        option1 = st.selectbox(
            "Choose card to update",
            ("simplii", "tangerine", "bmo", "mbna", "rbc"),
            index=None,
            placeholder="Select card to edit",
        )
        if option1 :
            if option1 == "simplii":
                 confirm_income("card",option1,value)
            if option1 == "tangerine":
                 confirm_income("card",option1,value)
            if option1 == "bmo":
                 confirm_income("card",option1,value)
            if option1 == "mbna":
                if confirm():
                     confirm_income("card", option1, value)
            if option1 == "rbc":
                 confirm_income("card",option1,value)

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
        if option :
            if option == "simplii":
                confirm_expense("card",option,value)
            if option == "tangerine":
                confirm_expense("card",option,value)
            if option == "bmo":
                confirm_expense("card",option,value)
            if option == "mbna":
                confirm_expense("card",option,value)
            if option == "rbc":
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
            if option:
                if option == "simplii":
                    confirm_add("card", option, new)
                if option == "tangerine":
                    confirm_add("card", option, new)
                if option == "bmo":
                    confirm_add("card", option, new)
                if option == "mbna":
                    confirm_add("card", option, new)
                if option == "rbc":
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


with open('dictionary.txt') as file:  # Reading the file here
    data = json.load(file)
file.close()

# components.html("""<html><body><h1>:)</h1></body></html>""",height=70)

show = st.button("Show Balance")
edit= st.toggle("Edit")
calculate = st.toggle("calculate",disabled=edit)

if show :
    st.write('Total balance remaining:', data["total"]["total"])
elif edit:
    type = st.radio(
        "Total",
        [":green[INCOME]", ":red[EXPENSE]","add"], index=None, horizontal=True,
        captions=[":money_mouth_face:", ":pinched_fingers:"])

    if type == ":green[INCOME]":
        try:
            income = st.number_input(label="Enter paid amount", value=None, placeholder="")
            add(income,"income")
        except TypeError:
            st.write("enter number")

    elif type == ":red[EXPENSE]":
        try:
            expense = st.number_input(label="Enter expense amount", value=None)
            add(expense,"expense")
        except TypeError:
            st.write("enter number")
    elif type=="add":
        add()

elif calculate:
    monthly=1
    monthly=st.number_input("Enter monthly Payments:",value=1.0)
    months=data["total"]["total"]/monthly
    st.write(f"Debt free in {months} Months 	:relieved:")

balance()


