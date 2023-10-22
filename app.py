from altair.vegalite.v4.api import Chart
import streamlit as st 
from dotenv import load_dotenv
import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from streamlit_extras.add_vertical_space import add_vertical_space
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.callbacks import get_openai_callback
import os

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

    load_dotenv()
    st.write("hello")

    # Upload  PDF
    pdf=st.file_uploader("Upload your pdf",type='pdf')
    if pdf is not None:

     pdf_reader=PdfReader(pdf)
     st.write(pdf.name)

     store_name=pdf.name[:-4]

     text=""

     for pages in pdf_reader.pages:

        text +=pages.extract_text()
     st.write(text)
     text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
            )
     chunks=text_splitter.split_text(text=text)
    
    
     #emmbedding
     if os.path.exists(f"{store_name}.pkl"):
        with open(f"{store_name}.pkl", "rb") as f:
            VectorStore = pickle.load(f)
            # st.write('Embeddings Loaded from the Disk')s
     else:
        embeddings = OpenAIEmbeddings()
        VectorStore = FAISS.from_texts(chunks, embedding=embeddings)
        with open(f"{store_name}.pkl", "wb") as f:
            pickle.dump(VectorStore, f)
    

     #Accept user question
     query = st.text_input("Ask questions about your PDF file:")
        # st.write(query)
 
    if query:
            docs = VectorStore.similarity_search(query=query, k=3)
 
            llm = OpenAI()
            chain = load_qa_chain(llm=llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=query)
                print(cb)
            st.write(response)




if __name__=='__main__':
    
     main()
   