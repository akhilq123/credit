import streamlit as st
import json

with open("Multipage/pages/dictionary.txt") as file:  # Reading the file here
    data = json.load(file)
    file.close()

def write_json(content,filepath="Multipage/pages/dictionary.txt"):
    with open(filepath, 'w') as file:  # Writing to file here
        file.write(json.dumps(content))
def add(type,merch,amount):

    if merch in ("scotia_loc","rbc_loc"):
        if type ==":green[INCOME]":
            data["loc"][merch] -= amount
        elif type == ":red[EXPENSE]":
            data["loc"][merch] += amount
    else:
        if type == ":green[INCOME]":
            data["card"][merch] -= amount
        elif type == ":red[EXPENSE]":
            data["card"][merch] += amount
    confirm = st.button("SAVE")
    if confirm:
        write_json(data,"pages/dictionary.txt")

def new_merchant():
    type = st.radio("What do you want to add",
    ["loc", "card","other"], index=None,horizontal=True,
    captions = ["Line Of Credit", "Credit Card","Everything Else"])
    if type:
        merchant = st.text_input("Enter Merchant Name")
        amount = st.number_input("Enter amount")
        data[type][merchant]=amount
        confirm=st.button("SAVE")
        if confirm:
            write_json(data)

def delete():
    x=1
    for i, j in data.items():
        if i == "total":
            continue
        for k, l in j.items():
            st.write(k, l)
            x+=x
            confirm = st.button("DELETE",key=x)
            if confirm :
                st.write(k,":",data[i][k],"Deleted")
                del data[i][k]
                write_json(data)
                break

tab1, tab2, tab3 = st.tabs(["Record transaction", "Add", "Remove"])

with tab1:
    option = st.selectbox(
        "Choose Merchant",
        ("scotia_loc", "rbc_loc", "Cad", "simplii", "tangerine", "bmo", "mbna", "rbc", "cad_tire"),
        index=None,
        placeholder="Select contact method...",
    )
    type = st.radio(
        "Total",
        [":green[INCOME]", ":red[EXPENSE]"], index=None, horizontal=True,
        captions=[":money_mouth_face:", ":pinched_fingers:"])
    try:
        amount = st.number_input(label="Enter amount", value=None, placeholder="")
        add(type, option, amount)
    except TypeError:
        st.write("enter number")

with tab2:
    try:
        new_merchant()
    except KeyError:
        st.write("")

with tab3:
   st.header("Line Of Credit Remaining:")
   delete()

st.title("Edit Record Book")
choose = st.radio("What do you want to edit",
    ["Record transaction", "Add","Remove"], index=None,horizontal=True,
    captions = ["Payment OR Expense", "New Merchant","Remove Merchant"])

if choose == "Record transaction" :
    option = st.selectbox(
        "Choose Merchant",
        ("scotia_loc", "rbc_loc", "Cad","simplii","tangerine","bmo","mbna","rbc","cad_tire"),
        index=None,
        placeholder="Select contact method...",
    )
    type = st.radio(
        "Total",
        [":green[INCOME]", ":red[EXPENSE]"], index=None, horizontal=True,
        captions=[":money_mouth_face:", ":pinched_fingers:"])
    try:
        amount = st.number_input(label="Enter amount", value=None, placeholder="")
        add(type,option,amount)
    except TypeError:
        st.write("enter number")
elif choose == "Add":
    try:
        new_merchant()
    except KeyError:
        st.write("")
elif choose == "Remove":
    # del data["loc"]["gdsf"]
    delete()

# for i,j in data.items():
#     for k,l in j.items():
#         st.write(k,l)
#         st.session_state[k]=l

# st.session_state
# st.write(data)
