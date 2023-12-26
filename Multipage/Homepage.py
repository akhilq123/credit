import streamlit as st
import json
with open("Multipage/pages/dictionary.txt") as file:  # Reading the file here
    data = json.load(file)
    file.close()
def write_json(content,filepath="Multipage/pages/dictionary.txt"):
    with open(filepath, 'w') as file:  # Writing to file here
        file.write(json.dumps(content))
def total():
    for i, j in data.items():
        if i == "loc":
            total1=0
            for k, l in j.items():
                total1 = total1 + l
            data["total"]["loc_total"] = total1.__round__(2)
        elif i == "card":
            total2=0
            for k, l in j.items():
                total2 = total2 + l
            data["total"]["card_total"] = total2.__round__(2)
        elif i == "other":
            total3=0
            for k, l in j.items():
                total3 = total3 + l
                data["total"]["other_total"] = total3.__round__(2)
    write_json(data)

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
img1 = "https://wealthywomanfinance.com/wp-content/uploads/2023/05/money-vision-board-examples-1000-%C3%97-600-px-1200-%C3%97-800-px-1.jpg"
st.image(img1, caption='Together We Can! ')
tab1, tab2, tab3, tab4 = st.tabs(["TOTAL", "CARD", "LOC", "other"])
tot = total()
with tab1:
   st.header("Total Remaining")
   total=0
   for i,j in data.items():
       if i == "total":
           continue
       for k,l in j.items():
           total= total+l
   data["total"]["total"] = total.__round__(2)
   write_json(data)
   st.write(data["total"]["total"])
   month = data["total"]["total"] / 2000
   payment = data["total"]["total"] / 12
   st.write(f"Dream of house just {month.__round__(0)} MONTHS away if you save 2000 a month")
   st.write(f"If you want to clear the debt within an year you have to pay {payment.__round__(0)} Dollars Monthly")

with tab2:
   st.header("Card Remaining")
   st.write(data["total"]["card_total"])
   total1 = 0
   for i, j in data.items():
       if i == "card":
           for k, l in j.items():
               st.write(f" {k}  :  {l}")


with tab3:
   st.header("Line Of Credit Remaining:")
   st.write(data["total"]["loc_total"])
   for i, j in data.items():
       if i == "loc":
           for k, l in j.items():
               st.write(f" {k}  :  {l}")



with tab4:
    st.header("other Debts Remaining:")
    st.write(data["total"]["other_total"])
    for i, j in data.items():
        if i == "other":
            for k, l in j.items():
                st.write(f" {k}  :  {l}")





# if "my_input" not in st.session_state:
#     st.session_state["my_input"]=""
#
# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

