import streamlit as st
import re

st.title("Fill-in-the-Blanks Generator")

# Input text area
text_input = st.text_area("Enter your text here:", height=250)

# Input for the word interval (e.g., every nth eligible word)
word_interval = st.number_input("Enter the interval (e.g., every nth eligible word to hide):", min_value=1, value=5, step=1)

# Input for the minimum word length to be considered eligible
min_word_length = st.number_input("Enter minimum word length to consider for hiding:", min_value=1, value=3, step=1)

# Input for the maximum word length to be considered eligible
max_word_length = st.number_input("Enter maximum word length to consider for hiding:", min_value=1, value=9, step=1)

if st.button("Generate"):
    if text_input:
        # Split the text into tokens: words and non-word tokens (punctuation, spaces, etc.)
        tokens = re.split(r'(\W+)', text_input)
        
        eligible_count = 0
        # Iterate over tokens: process only tokens that are pure word characters (no punctuation)
        for i, token in enumerate(tokens):
            if re.fullmatch(r'\w+', token):  # Check if token is a word (letters, digits, underscore)
                if len(token) >= min_word_length and len(token) <= max_word_length:
                    eligible_count += 1
                    if eligible_count % word_interval == 0:
                        # Replace the word with dashes equal to its length
                        tokens[i] = '- ' * len(token)
        
        # Reassemble tokens into the output text, preserving punctuation and spaces
        output_text = ''.join(tokens)
        st.subheader("Output:")
        st.write(output_text)
    else:
        st.error("Please enter some text!")
