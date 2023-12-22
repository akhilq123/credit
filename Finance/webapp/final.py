import streamlit as st
import functions
import json
import streamlit.components.v1 as components

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
            functions.add(income,"income")
        except TypeError:
            st.write("enter number")

    elif type == ":red[EXPENSE]":
        try:
            expense = st.number_input(label="Enter expense amount", value=None)
            functions.add(expense,"expense")
        except TypeError:
            st.write("enter number")
    elif type=="add":
        functions.add()

elif calculate:
    monthly=1
    monthly=st.number_input("Enter monthly Payments:",value=1.0)
    months=data["total"]["total"]/monthly
    st.write(f"Debt free in {months} Months 	:relieved:")

functions.balance()


