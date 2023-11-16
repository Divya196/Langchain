# Q&A Chatbot
from langchain.llms import OpenAI

#from dotenv import load_dotenv

#load_dotenv()  # take environment variables from .env.

import streamlit as st
import os

#from dotenv import load_dotenv,find_dotenv
#load_dotenv(find_dotenv())


## Function to load OpenAI model and get respones
#OpenAI_key = os.environ.get("OPENAI_API_KEY")
#print(OpenAI_key)

def get_openai_response(question):
    #llm=OpenAI(openai_api_key= OpenAI_key,model_name="text-davinci-003",temperature=0.5)
    llm=OpenAI(model_name="text-davinci-003",temperature=0.5)
    response=llm(question)
    return response


##initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

## If ask button is clicked

if submit:
    st.subheader("The Response is")
    st.write(response)





#import streamlit as st

#"Hello, World!"


