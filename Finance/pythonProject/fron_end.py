import streamlit as st
from modules import functions

contents = functions.get_todo()
st.write(contents)


option = st.selectbox(
   "What would you like to do: ",
   ("Show Balance", "Edit Balance", "Calculate"),
   index=None,
   placeholder="Please Select",
)

st.write('You selected:', option)

if option == "Show Balance" :
    st.write('Total balance remaining:',contents[0])

elif option == "Edit Balance":
        type = st.radio(
            "Total",
            [":green[INCOME]", ":red[EXPENSE]"],
            index=None,
            captions=[":money_mouth_face:", ":pinched_fingers:"])
        if type == ":green[INCOME]" :
            try:
                income =st.number_input(label="Enter paid amount",value=None,placeholder="")
                new_debt = float(contents[0])-income
                st.write(f"Do you want to save the updated balance: :green[{new_debt}] from:  :red[{contents[0]}] ")
                confirmation = st.radio(
                                    "Total",
                                    [":red[Yes]",":green[No]"],
                                    index=None)

                if confirmation == ":red[Yes]":
                    contents.insert(0,f"{new_debt}" +"\n")
                    contents.pop(1)
                    functions.write_todo(contents)
            except TypeError :
                st.write("enter number")
        elif type == ":red[EXPENSE]":
            try:
                expense = st.number_input(label="Enter expense amount",value=None)
                new_debt= float(contents[0])+ expense
                st.write(f"Do you want to save the updated balance: :green[{new_debt}] from:  :red[{contents[0]}] ")
                confirmation = st.radio(
                    "Total",
                    [":red[Yes]", ":green[No]"],
                    index=None)
                if confirmation == ":red[Yes]":
                    contents.insert(0, f"{new_debt}" + "\n")
                    contents.pop(1)
                    functions.write_todo(contents)
            except TypeError:
                st.write("enter number")
