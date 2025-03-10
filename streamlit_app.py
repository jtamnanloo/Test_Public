import streamlit as st
import random

st.title("Fill-in-the-Blanks Generator")

# Input text area
text_input = st.text_area("Enter your text here:", height=100)

# Input for percentage
percentage = st.number_input("Enter percentage of words to replace (0-100):", min_value=0, max_value=100, value=20, step=1)

if st.button("Generate"):
    if text_input:
        words = text_input.split()
        # Calculate number of words to replace (at least 1)
        num_to_replace = max(1, int(len(words) * (percentage / 100)))
        indices = random.sample(range(len(words)), num_to_replace)
        for i in indices:
            words[i] = "_____"
        output_text = " ".join(words)
        st.subheader("Output:")
        st.write(output_text)
    else:
        st.error("Please enter some text!")
