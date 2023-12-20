import streamlit as st
from modules import functions

st.title("My To Do App")
st.subheader("This App is to increase productivity")

todos = functions.get_todo()

def add_todo() :
    todo = st.session_state["new_todo"]+"\n"
    todos.append(todo)
    functions.write_todo(todos)



for index, todo in enumerate(todos) :
    value = st.checkbox(todo,key=todo)
    if value:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.rerun()
st.text_input("",placeholder= "Enter as todo",
              on_change=add_todo,key='new_todo')

# st.session_state is the dictionary to get the user inputs on the webapp
# to see the dictionary on web ap itself to better understand:
st.session_state