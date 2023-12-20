import streamlit as st
from modules import functions
import json

with st.form("my form") :
    with open('files/dictionary.txt') as file:  # Reading the file here
        data = json.load(file)
    file.close()

    option = st.selectbox(
        "What would you like to do: ",
        ("Show Balance", "Edit Balance", "Calculate"),
        index=None,
        placeholder="Please Select",
    )
    if option == "Show Balance":
        st.write('Total balance remaining:', data["total"])

    elif option == "Edit Balance":
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
                confirmation = st.radio(
                    "Total",
                    [":red[Yes]", ":green[No]"],
                    index=None, horizontal=True)

                if confirmation == ":red[Yes]":
                    data = functions.read_json()
                    data["total"] = new_debt
                    functions.write_json(data)

            except TypeError:
                st.write("enter number")
        elif type == ":red[EXPENSE]":
            try:
                expense = st.number_input(label="Enter expense amount", value=None)
                new_debt = float(data["total"]) + expense
                old = data["total"]
                st.write(f"Do you want to save the updated balance: :green[{new_debt}] from:  :red[{old}] ")
                confirmation = st.radio(
                    "Total",
                    [":red[Yes]", ":green[No]", ":white[EXIT]"],
                    index=None,
                    horizontal=True)
                if confirmation == ":red[Yes]":
                    # data = functions.read_json()
                    # data["total"] = new_debt
                    # functions.write_json(data)
                    def form_callback():
                        st.write(st.session_state.my_slider)
                        st.write(st.session_state.my_checkbox)


                    functions.altering_element("total", new_debt)
                    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)
            except TypeError:
                st.write("enter number")
    st.form_submit_button("hi")
