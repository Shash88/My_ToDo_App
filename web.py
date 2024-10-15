import streamlit as st
from functions import get_todo, write_todo

todos = get_todo()

def add_todo():
  todo = st.session_state["new_todo"] + "\n"
  todos.append(todo)
  write_todo(todos)

st.title("My To-Do App")
st.subheader("This is my To-Do web app")
st.write("The app is meant to increase one's productivity")

for index, todo in enumerate(todos):
  check_box = st.checkbox(todo, key=todo)
  if check_box:
    todos.pop(index)
    write_todo(todos)
    del st.session_state[todo]
    st.rerun()

st.text_input(label="Type a ToDo", label_visibility='collapsed', placeholder="Add a new todo...", on_change=add_todo, key='new_todo')