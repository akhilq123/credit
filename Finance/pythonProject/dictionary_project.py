import streamlit as st
import json

# with open("files/dictionary.txt", "r") as files:
#     local_todos = files.readlines()
# st.write(local_todos[0].split("[")[2])
#
# re=local_todos[0].split("[")[2]
# st.write(re[0:-1])

a = {
    "loc": {"scotia":3500,"rbc":10000},
    "card": {"simplii":100,"tangerine":200,"bmo":111,"mbna":555,"rbc":557},
    "total":7777
}
with open('files/dictionary.txt', 'w') as file:    # Writing to file here
    file.write(json.dumps(a))
file.close()
with open('files/dictionary.txt') as file:         # Reading the file here
    data = json.load(file)
file.close()
    st.write(type(data))
    data["LOC"]=100
st.write(data)

with open('files/dictionary.txt', 'w') as file:    # Writing to file here
    file.write(json.dumps(data))
file.close()