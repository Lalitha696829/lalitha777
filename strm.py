import streamlit as st

# Title
st.title("My Streamlit App")

# Button
if st.button("Click Me!"):
    st.write("Button Clicked!")

# Slider
value = st.slider("Select a value", 0, 100, 50)
st.write(f"Slider value: {value}")

# Display Image with Caption
