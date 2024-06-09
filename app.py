import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def translate_word(word, target_language):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.7,
        messages=[
            {"role": "system", "content": "Translate the word to another language."},
            {"role": "user", "content": f">>Word: {word}\n\n>>Target Language: {target_language}"},
        ]
    )
    return response.choices[0].message.content

# Streamlit app code
st.title("Word Translator")
word = st.text_input("Enter a word:")
target_language = st.selectbox("Select target language:", ["English", "Arabic", "French", "Spanish", "German"])

if st.button("Translate"):
    if word.strip() == "":
        st.error("Please enter a word.")
    else:
        translation = translate_word(word, target_language)
        st.success(f"Translation: {translation}")