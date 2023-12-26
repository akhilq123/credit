import streamlit as st
import json
with open("Multipage/pages/dictionary.txt") as file:  # Reading the file here
    data = json.load(file)
    file.close()
def write_json(content,filepath="Multipage/pages/dictionary.txt"):
    with open(filepath, 'w') as file:  # Writing to file here
        file.write(json.dumps(content))

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
img1 = "https://wealthywomanfinance.com/wp-content/uploads/2023/05/money-vision-board-examples-1000-%C3%97-600-px-1200-%C3%97-800-px-1.jpg"
st.image(img1, caption='Together We Can! ')
tab1, tab2, tab3, tab4 = st.tabs(["TOTAL", "CARD", "LOC", "other"])

with tab1:
   st.header("Total Remaining")
   total=0
   for i,j in data.items():
       if i == "total":
           continue
       for k,l in j.items():
           st.write(f" {k}  :  {l}")
           total= total+l
   data["total"]["total"] = total.__round__(2)
   write_json(data)
   st.write(data["total"]["total"])

with tab2:
   st.header("Card Remaining")
   total1 = 0
   for i, j in data.items():
       if i == "card":
           for k, l in j.items():
               total1 = total1 + l
               st.write(f" {k}  :  {l}")
   data["total"]["card_total"] = total1.__round__(2)
   write_json(data)
   st.write(data["total"]["card_total"])

with tab3:
   st.header("Line Of Credit Remaining:")
   total1 = 0
   for i, j in data.items():
       if i == "loc":
           for k, l in j.items():
               st.write(f" {k}  :  {l}")
               total1 = total1 + l
   data["total"]["loc_total"] = total1.__round__(2)
   write_json(data)
   st.write(data["total"]["loc_total"])

with tab4:
    st.header("other Debts Remaining:")
    total1 = 0
    for i, j in data.items():
        if i == "other":
            for k, l in j.items():
                st.write(f" {k}  :  {l}")
                total1 = total1 + l
    data["total"]["other"] = total1.__round__(2)
    write_json(data)
    st.write(data["total"]["other"])



month = data["total"]["total"]/2000
payment = data["total"]["total"]/12
st.write(f"Dream of house just {month.__round__(0)} MONTHS away if you save 2000 a month")
st.write(f"If you want to clear the debt within an year you have to pay {payment.__round__(0)} Dollars Monthly")
st.sidebar.success("Select a page above.")

# if "my_input" not in st.session_state:
#     st.session_state["my_input"]=""
#
# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

