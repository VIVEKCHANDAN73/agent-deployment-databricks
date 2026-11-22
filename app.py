import streamlit as st
from agent import get_response

st.title("My Databricks AI Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

query = st.chat_input("Ask something...")

if query:
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.write(query)

    with st.chat_message("assistant"):
        response = get_response(query)
        st.write(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })