import os
import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from tempfile import NamedTemporaryFile 
from dotenv import load_dotenv


def main():
  # page configuration and styling

  st.set_page_config(page_title='ask CSV files',layout="centered",initial_sidebar_state="collapsed",

  # page_icon="loogo.jpg",
    menu_items={
        'Get Help': 'https://github.com/regnna',
        'Report a bug': 'https://github.com/regnna',
        'About': 'Regnna'
    })
  style="""<style>

  .stApp {
      margin: auto;
      font-family: -apple-system, BlinkMacSystemFont, sans-serif;
      overflow: auto;
      background: linear-gradient(315deg, #4f2991 3%, #7dc4ff 38%, #36cfcc 68%, #a92ed3 98%);
      animation: gradient 15s ease infinite;
      background-size: 400% 400%;
      background-attachment: fixed;
  }
  .stTextInput>label {
      font-size:140%; 
      font-weight:bold; 
      color:white; 
      # background:linear-gradient(to bottom, #3399ff 0%,#00ffff 100%);
      # border: 10px;
      # border-radius: 90px;
    } 
    .stHeader{
    background-color: transparent;
      font-family:BlinkMacSystemFont;
      text-align:center;
      color: #2E475D; 
    }
  </style>
  """

  hide_st_style="""
                  <style>
                  #MainMenu {visibility:hidden;}
                  header{visibility:hidden;}
                  footer{visibility:hidden;}
                  </style>
                  """
  st.markdown(style,unsafe_allow_html=True)
  st.markdown(hide_st_style,unsafe_allow_html=True)

  # contains of the web
  # load_dotenv()
  
  # if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
  #       print("OPENAI_API_KEY is not set")
  #       exit(1)
  # else:
  #       print("OPENAI_API_KEY is set")
  st.markdown("<h1 style='text-align: center; color: white;'>Ask your csv</h1>",unsafe_allow_html=True)
  st.markdown(" <a href='https://platform.openai.com/account/api-keys'>openai API key</a>",unsafe_allow_html=True)
  openaikey=st.text_input("Enter your <a href='https://platform.openai.com/account/api-keys'>openai API key</a>",unsafe_allow_html=True)

  # st.header("Ask Your CSV ")
  user_csv=st.file_uploader("Upload your CSV file",type="csv")
  # st.markdown(openaikey)
  t=openaikey == ""
  # st.markdown(t)
  if user_csv is not None:
        with NamedTemporaryFile(mode='w+b', suffix=".csv") as f:
            os.environ["OPENAI_API_KEY"]=openaikey
            f.write(user_csv.getvalue())
            llm = OpenAI(temperature=0)
            user_input = st.text_input("Question here:")
            agent = create_csv_agent(llm, f.name, verbose=True)
            if user_input:
                response = agent.run(user_input)
                st.write(response)
            f.flush()
            
  # if user_csv is not None:
  #   with NamedTemporaryFile() as f:
  #           f.write(user_csv.getvalue())
  #           # f.flush()
  #           user_question=st.text_input("Ask a question about your CSV",disabled=t,placeholder="Enter your Question")
  #           llm=OpenAI(temperature=0)
  #           agent = create_csv_agent(
  #                   OpenAI(temperature=0), f.name, verbose=True)

  #           user_question=st.text_input("Ask a question about your CSV",disabled=t,placeholder="Enter your Question")
  #           if user_question is not None and user_question!="":
  #             st.write(f"Your Question is: {user_question}")
  #             response=agent.run(user_question)


if __name__=="__main__":
  main()
