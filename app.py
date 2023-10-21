import streamlit as st 
from altair.vegalite.v4 import Chart
from streamlit_extras.add_vertical_space import add_vertical_space

with st.sidebar:
    st.title("LLM Chat")
    st.markdown('''
        #About
        This application is an LLM-based chatbot built using:
         - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    '''
    )