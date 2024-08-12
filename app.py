
import streamlit as st
from pages import home, grammar_fun, reading_translation, testAudioRecord

PAGES = {
    "Home": home,
    "Grammar and Fun": grammar_fun,
    "Reading and Translation": reading_translation,
    "Recorder Demo":testAudioRecord
}

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))

    page = PAGES[selection]
    page.app()

if __name__ == "__main__":
    main()
