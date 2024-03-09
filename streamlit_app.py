


from langchain_experimental.agents import create_csv_agent
from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
import openai
from langchain_openai import OpenAI


def main():
    load_dotenv()
    print("DEBUG: OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
    st.set_page_config(page_title="Sage-Bot", page_icon="favicon.ico", layout="wide", initial_sidebar_state="expanded")
    
    st.markdown(
        """
        <style>
            body {
                background-color: white !important;
            }
            .sidebar .sidebar-content {
                background-color: white !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


    openai_api_key = os.getenv("OPENAI_API_KEY")
    if openai_api_key is None or openai_api_key.lower() == "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":
        print("ERROR: OPENAI_API_KEY is not set or incorrect")
        print("OPENAI_API_KEY is not set")
        exit(1)
    else:
        print("OPENAI_API_KEY is set")
   

    # Add name at the bottom of the sidebar




    st.header("Lets Handle the Stats 📈 ")
    st.header("ASK ME about $Sage! My Pal ")
    

    #st.image("logo.jpg", caption="Your Image Caption", use_column_width=True)

    selected_category = st.radio("Select Services", ["My Sage","Sage-AI","Sage-ML","Sage-Crypt",])

    datasets = {
        "My Sage": "D:\EY\langchain\Alchathon-Dataset.csv",
        "Sage-AI": "D:\EY\langchain\Alchathon-Dataset.csv",
        "Sage-Ml": "D:\EY\langchain\Alchathon-Dataset.csv",
        "Sage-Crypt" : "D:\EY\langchain\Alchathon-Dataset.csv",
    }

    csv_file_path = datasets.get(selected_category)
    if csv_file_path is not None:

        agent = create_csv_agent(
            OpenAI(api_key="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", temperature=0),
            csv_file_path,
            verbose=True
        )

        user_question = st.text_input("Ask a question : ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))

if __name__ == "__main__":
    main()