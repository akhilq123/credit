import streamlit as st
import json


with open("Multipage/pages/dictionary.txt") as file:  # Reading the file here
    data = json.load(file)
    file.close()

tab1, tab2 = st.tabs(["Months Remaining", "Monthly Payement"])

with tab1:
   st.header("Total Remaining")
   try:
       monthly_payment = st.number_input("Enter monthly payment",key="payment")
       months = data["total"]["total"] / monthly_payment
       st.write("You will be debt free in ", months.__round__(2), "Months")
   except ZeroDivisionError:
       st.write("")

with tab2:
   st.header("Card Remaining")
   try:
       month = st.number_input("Enter the number of months to target date",key="month")
       payment = data["total"]["total"] / month
       st.write("In order to be Debt free in ", month, " months ", "You have to pay ", payment.__round__(2),
                "Every month")
   except ZeroDivisionError:
       st.write("")
