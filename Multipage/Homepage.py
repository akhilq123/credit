import streamlit as st
import json
with open("Multipage/pages/dictionary.txt") as file:  # Reading the file here
    data = json.load(file)
    file.close()

st.set_page_config(
    page_title="Multipage App",
    page_icon="👋",
)
img1 = "https://wealthywomanfinance.com/wp-content/uploads/2023/05/money-vision-board-examples-1000-%C3%97-600-px-1200-%C3%97-800-px-1.jpg"
st.image(img1, caption='Together We Can! ')
tab1, tab2, tab3 = st.tabs(["TOTAL", "CARD", "LOC"])

with tab1:
   st.header("Total Remaining")
   st.write(data["total"]["total"])

with tab2:
   st.header("Card Remaining")
   st.write(data["total"]["card_total"])

with tab3:
   st.header("Line Of Credit Remaining:")
   st.write(data["total"]["loc_total"])
month = data["total"]["total"]/2000
st.write(f"Dream of house just {month.__round__(0)} MONTHS away if you save 2000 a month")
st.sidebar.success("Select a page above.")

# if "my_input" not in st.session_state:
#     st.session_state["my_input"]=""
#
# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)

