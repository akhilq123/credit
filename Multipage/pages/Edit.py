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
    elif merch in ("simplii", "tangerine", "bmo", "mbna", "rbc", "cad_tire"):
        if type == ":green[INCOME]":
            data["card"][merch] -= amount
        elif type == ":red[EXPENSE]":
            data["card"][merch] += amount
    else:
        if type == ":green[INCOME]":
            data["other"][merch] -= amount
        elif type == ":red[EXPENSE]":
            data["other"][merch] += amount
    confirm = st.button("SAVE")
    if confirm:
        write_json(data)

def new_merchant():
    type = st.radio("What do you want to add",
    ["loc", "card","other"], index=None,horizontal=True,
    captions = ["Line Of Credit", "Credit Card","Everything Else"])
    if type:
        merchant = st.text_input("Enter Merchant Name")
        amount = st.number_input("Enter amount")
        data[type][merchant]=amount
        confirm=st.button("SAVE",key="new_merch")
        if confirm:
            write_json(data)

def delete():
        with st.form("H"):
            x=1
            for i, j in data.items():
                if i == "total":
                    continue
                for k, l in j.items():
                    st.write(k, l)
                    x+=x
                    confirm = st.checkbox(f"DELETE {k}",key=x)
                    if confirm :
                        tog = st.text_input(f"{k}:{data[i][k]} will be Deleted,type confirm to Delete")
                        if tog =="confirm":
                            st.write("DELETED!")
                            del data[i][k]
                            write_json(data)
                            break
            hi =st.form_submit_button("Refresh")


st.title("Edit Record Book")

tab1, tab2, tab3, tab4 = st.tabs(["Record transaction", "Add","Edit","Remove"])

with tab1:
    st.header("Details of payment")
    option = st.selectbox(
        "Choose Merchant payed",
        ("scotia_loc", "rbc_loc", "simplii", "tangerine", "bmo", "mbna", "rbc","other"),
        index=None,
        placeholder="Select merchant",
    )
    if option == "other":
        oth = st.text_input("Enter the merchant name as exactly in records")
        values = list(data["other"].keys())
        for value in values:
            if value==oth:
                type = st.radio(
                    "Total",
                    [":green[INCOME]", ":red[EXPENSE]"], index=None, horizontal=True,
                )
                try:
                    amount = st.number_input(label="Enter amount", value=None, placeholder="")
                    add(type, oth, amount)
                except TypeError:
                    st.write("enter number")
    else:
        if option:
            type = st.radio(
                "Total",
                [":green[INCOME]", ":red[EXPENSE]"], index=None, horizontal=True,
            )
            if type:
                try:
                    amount = st.number_input(label="Enter amount", value=None, placeholder="")
                    add(type, option, amount)
                except TypeError:
                    st.write("enter number")
with tab2:
    try:
        st.header("Enter details of New Merchant")
        new_merchant()
    except KeyError:
        st.write("")

with tab3:
    option = st.selectbox(
        "Choose Merchant payed",
        ("scotia_loc", "rbc_loc", "simplii", "tangerine", "bmo", "mbna", "rbc", "other"),
        index=None,
        placeholder="Select merchant",
        key="tab2"
    )
    if option == "other":
        oth = st.text_input("Enter the merchant name as exactly in records")
        values = list(data[option].keys())
        for value in values:
            if value == oth:
                try:
                    amount = st.number_input(label="Enter amount", value=None, placeholder="")
                    data[option][oth]= amount
                    confirm = st.button("SAVE")
                    if confirm:
                        st.write(f"{oth} : {data[option][oth]} SAVED")
                        write_json(data)
                except TypeError:
                    st.write("enter number")

    else:
        if option:
            try:
                amount = st.number_input(label="Enter amount", value=None, placeholder="")
                if option in ("scotia_loc", "rbc_loc"):
                    parent_key = "loc"
                    data[parent_key][option]= amount
                    confirm = st.button("SAVE")
                    if confirm:
                        st.write(f"{option} : {data[parent_key][option]} SAVED")
                        write_json(data)
                else :
                    parent_key = "card"
                    data[parent_key][option] = amount
                    confirm = st.button("SAVE")
                    if confirm:
                        st.write(f"{option} : {data[parent_key][option]} SAVED")
                        write_json(data)


            except TypeError:
                st.write("enter number")

with tab4:
   st.header("Chose the record to be deleted")
   delete()


