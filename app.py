from altair.vegalite.v4.api import Chart
import streamlit as st 
from PyPDF2 import PdfReader
from streamlit_extras.add_vertical_space import add_vertical_space

with st.sidebar:

    st.title("LLM Chat")
    st.markdown('''
        #About
        This application is an LLM-based chatbot built using:
         - [Streamlit](https://streamlit.io/)
         - [LangChain](https://python.langchain.com/)
         - [OpenAI](https://platform.openai.com/docs/models) 
 
    '''
    )


def main():
    
    st.write("hello")

    # Upload  PDF
    pdf=st.file_uploader("Upload your pdf",type='pdf')
    if pdf is not None:

     pdf_reader=PdfReader(pdf)

     text=""

     for pages in pdf_reader.pages:

        text +=pages.extract_text()
     st.write(text)





if __name__=='__main__':
    
     main()
   