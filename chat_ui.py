import streamlit as st
from streamlit_chat import message  # Ensure streamlit_chat is installed

def chatbot_ui(messages, user_input, is_processing, on_submit):
    """
    Renders the chatbot UI using Streamlit and streamlit-chat.
    :param messages: List of conversation history.
    :param user_input: Current user input.
    :param is_processing: Boolean indicating if the app is processing.
    :param on_submit: Callback function to handle form submission.
    """
    st.title("AI Gift Suggestion Chatbot")

    # Display chat history
    for msg in messages:
        if msg["role"] == "user":
            message(msg["content"], is_user=True)
        elif msg["role"] == "assistant":
            message(msg["content"])

    # Input form
    with st.form(key="chat_input_form"):
        st.text_input(
            "Type your message here:",
            value=user_input,
            key="user_input",
            placeholder="Type your message...",
        )
        submit_button = st.form_submit_button("Send", on_click=on_submit)

    # Spinner for processing
    if is_processing:
        with st.spinner("Processing... Please wait..."):
            pass