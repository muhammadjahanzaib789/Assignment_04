import streamlit as st

# Title and header
st.title("welcome to MY Python Website")
st.header("Explore Amazing Features")

# Adding some text
st.write("This is a simple Streamlit app built in just 15 minutes")

# Adding a button
if st.button("Click Me"):
    st.write("Thankyou for clicking the button!")

# Adding user input
name =st.text_input("What is your name ?")
if st.button ("Streamlit"):
    st.write(f"Hello, {name}! Welcome  to my website!")


         

