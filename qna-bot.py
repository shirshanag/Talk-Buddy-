from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm=ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite")

st.title(" 🤖 Talk Buddy ")
st.markdown("My QnA bot with langchain and Google Gemini !")
if "messages" not in st.session_state:
    st.session_state.messages=[]
for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)

query=st.chat_input("Ask Anything ?")

if query:
    #print(query)
    st.session_state.messages.append({"role":"user","content":query}) # Adding the questions into the history
    st.chat_message("user").markdown(query)

    res=llm.invoke(query)

    st.chat_message("AI").markdown(res.content[0]["text"])
    
    st.session_state.messages.append({"role":"AI","content":res.content[0]["text"]}) # Adding the answers in the history 

# while True:
#     query=input("User:")

#     if query.lower() in ["bye","quit","exit"]:
#         print("Good Bye!!")
#         break

#     res=llm.invoke(query)

#     print("AI:",res.content[0]["text"])

