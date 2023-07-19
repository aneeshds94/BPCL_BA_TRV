import streamlit as st
import time
import functions
import functions as func

current_time = time.time()

# Setting page width as wide
st.set_page_config(layout='wide')

# getting names from file
names = func.get_names()

# Three column heading layout
col1, col2, col3 = st.columns([0.5, 1, 0.5])
with col2:
    st.subheader("Indian Oil Corporation Ltd. Trivandrum AFS")
    st.subheader("BA Random Generator Tool")
st.info(time.strftime("%b %d, %Y %H:%M:%S"))
# Selection of shift
st.info("Select Shift: ")
col = st.columns(3)
for index, shift in enumerate(['A', 'B', 'C']):
    with col[index]:
        st.checkbox(shift)

# declaring in_shift variable
in_shift = []

# Selection of employees
st.info("Select employees available in shift from list below: ")
for index, name in enumerate(names):
    checkbox = st.checkbox(name, key=name[0:8])
    if checkbox:
        in_shift.append(name)

# Generate button
st.button("Generate", key="generate")

last_time = float(functions.get_time())

if current_time - last_time < 0 and st.session_state['generate']:
    random_name = functions.generate_name(in_shift)
    st.info(f"{random_name} {last_time} ")
    functions.post_time(current_time)

st.session_state
