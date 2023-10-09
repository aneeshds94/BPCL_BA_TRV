import streamlit as st
import functions
import timer

# Setting page width as wide
st.set_page_config(layout='wide')

# getting times
current_time = timer.get_current_time()
display_time, date = timer.get_display_datetime()
print(date)
last_time = float(functions.get_time())

# Heading area
st.subheader("Indian Oil Corporation Ltd. Calicut AFS")
st.subheader("BA Random Generator Tool")
st.info(display_time)

# Getting names from file
names = functions.get_names()
# declaring in_shift variable
in_shift = []
shifts = ['Select from dropdown',
          'A : 0600 hrs - 1400 hrs',
          'B : 1400 hrs - 2200 hrs',
          'C : 2200 hrs - 0600 hrs']

# Form
with st.form(key="ba_form"):
    shift = st.selectbox("Select shift from dropdown: ", shifts)

    # Selection of employees using checkbox
    st.info("Select employees available in shift from list below: ")
    for index, name in enumerate(names):
        checkbox = st.checkbox(name, key=index)
        if checkbox:
            in_shift.append(name)

    # Generate button
    button = st.form_submit_button("Generate")

    # Button press functionality
    if button and shift != 'Select from dropdown':
        # Checking time elapsed
        if current_time - last_time > 21600:
            random_name = functions.generate_name(in_shift, shift)
            random_display = f"{random_name} has been selected for BA test on \n" \
                             f"{date} for shift {shift}"
            st.info(random_display)
            functions.post_time(str(current_time))

        else:
            st.info("Button deactivated. Person already selected for BA test. "
                    )

    elif button and shift == 'Select from dropdown':
        st.info("Select shift!")
