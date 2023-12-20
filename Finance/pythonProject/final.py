import streamlit as st
from modules import functions
import json


with open('files/dictionary.txt') as file:  # Reading the file here
    data = json.load(file)
file.close()


show = st.button("Show Balance")
edit= st.toggle("Edit")
calculate = st.toggle("calculate",disabled=edit)

if show :
    st.write('Total balance remaining:', data["total"])
elif edit:
    type = st.radio(
        "Total",
        [":green[INCOME]", ":red[EXPENSE]"], index=None, horizontal=True,
        captions=[":money_mouth_face:", ":pinched_fingers:"])

    if type == ":green[INCOME]":
        try:
            income = st.number_input(label="Enter paid amount", value=None, placeholder="")
            new_debt = float(data["total"]) - income
            old = data["total"]
            st.write(f"Do you want to save the updated balance: :green[{new_debt}] from:  :red[{old}] ")
            confirmation = st.button("YES")
            if confirmation:
                data = functions.read_json()
                data["total"] = new_debt
                functions.write_json(data)
                st.write("Balance Updated")
        except TypeError:
            st.write("enter number")

    elif type == ":red[EXPENSE]":
        try:
            expense = st.number_input(label="Enter expense amount", value=None)
            new_debt = float(data["total"]) + expense
            old = data["total"]
            st.write(f"Do you want to save the updated balance: :green[{new_debt}] from:  :red[{old}] ")
            confirmation = st.button("SAVE")
            if confirmation :
                data = functions.read_json()
                data["total"] = new_debt
                functions.write_json(data)
                st.write("Balance Updated")
        except TypeError:
            st.write("enter number")
elif calculate:
    monthly=1
    monthly=st.number_input("Enter monthly Payments:",value=1.0)
    months=data["total"]/monthly
    st.write(f"Debt free in {months} Months 	:relieved:")
scotia_loc = data["loc"]["scotia"]
rbc_loc = data["loc"]["rbc"]
simplii = data["card"]["simplii"]
tangerine = data["card"]["tangerine"]
bmo = data["card"]["bmo"]
mbnna= data["card"]["mbna"]
rbc = data["card"]["rbc"]
if calculate ==False:
    st.write(data)