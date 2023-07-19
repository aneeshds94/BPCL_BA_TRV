import streamlit as st
import time
import functions

# Setting page width as wide
st.set_page_config(layout='wide')
# getting times
current_time = time.time()
last_time = float(functions.get_time())

# Heading area
st.subheader("Indian Oil Corporation Ltd. Trivandrum AFS")
st.subheader("BA Random Generator Tool")
st.info(time.strftime("%b %d, %Y %H:%M:%S"))

# Getting names from file
names = functions.get_names()
# declaring in_shift variable
in_shift = []

# Form
with st.form(key="ba_form"):
    # Selection of employees using checkbox
    st.info("Select employees available in shift from list below: ")
    for index, name in enumerate(names):
        checkbox = st.checkbox(name, key=index)
        if checkbox:
            in_shift.append(name)

    # Generate button
    button = st.form_submit_button("Generate")

    # Button press functionality
    if button:
        # Checking time elapsed
        if current_time - last_time > 30.0:
            random_name = functions.generate_name(in_shift)
            st.info(random_name)
            functions.post_time(str(current_time))
        else:
            st.info("Button deactivated")
