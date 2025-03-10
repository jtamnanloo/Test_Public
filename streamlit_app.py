import streamlit as st
import string

st.title("Fill-in-the-Blanks Generator")

# Input text area
text_input = st.text_area("Enter your text here:", height=400)

# Input for the word interval (e.g., every 3rd eligible word)
word_interval = st.number_input("Enter the interval (e.g., every nth eligible word to hide):", min_value=1, value=3, step=1)

# Input for the minimum word length to be considered eligible
min_word_length = st.number_input("Enter minimum word length to consider for hiding:", min_value=1, value=3, step=1)

if st.button("Generate"):
    if text_input:
        # Remove punctuation from the text
        clean_text = text_input.translate(str.maketrans('', '', string.punctuation))
        words = clean_text.split()

        eligible_count = 0
        # Replace every nth eligible word (only words with at least min_word_length letters)
        for i, word in enumerate(words):
            if len(word) >= min_word_length:
                eligible_count += 1
                if eligible_count % word_interval == 0:
                    # Replace the word with dashes equal to the length of the word
                    words[i] = "-" * len(word)
        
        output_text = " ".join(words)
        st.subheader("Output:")
        st.write(output_text)
    else:
        st.error("Please enter some text!")
