import streamlit as st
import functions as f
import time as t

tasks = f.get_tasks()

def add_task():
    new_task = st.session_state['new_task'].strip()
    if new_task:
        tasks = f.get_tasks()
        tasks.append(new_task + "\n")
        f.write_tasks(tasks)
    st.session_state['new_task'] = ""

now = t.strftime("%b-%d, %Y")

st.title("My Task App")
st.subheader(f"Today's Tasks: {now}")


for index, task in enumerate(tasks):
    key = f"{index}_{task}"  # e.g. "2_Third task\n"
    checkbox = st.checkbox(task, key=key)
    if checkbox:
        tasks.pop(index)
        f.write_tasks(tasks)
        del st.session_state[key]
        st.rerun()

st.text_input(label="", placeholder="Enter a Task", key="new_task",
              on_change=add_task, )

