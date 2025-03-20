import streamlit as st

# Title
st.title("Dynamic Streamlit App")

# Button
if st.button("Try Me!"):
    st.write("Button has been clicked!")

# Slider
value = st.slider("Pick a value", 10, 1000, 500)
st.write(f"Selected value: {value}")

# Display Image with Caption
st.image("https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0", caption="Stunning Nature View", use_column_width=True)
