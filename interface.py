import streamlit as st
from streamlit_chat import message  # Import the chat component

def chatbot_ui(messages, user_input, is_processing, on_submit):
    """
    Renders the chatbot interface using Streamlit-Chat components.
    :param messages: List of message dictionaries (user and assistant messages).
    :param user_input: Current user input.
    :param is_processing: Boolean indicating if the app is processing a response.
    :param on_submit: Callback function for user input submission.
    """
    st.title("AI Gift Suggestion Chatbot")

    # Display conversation history
    for i, msg in enumerate(messages):
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=f"user_{i}")
        elif msg["role"] == "assistant":
            message(msg["content"], key=f"assistant_{i}")

    # User input field
    st.write("---")
    st.text_input(
        "Type your message:",
        value=user_input,
        placeholder="Type your message here...",
        key="user_input",
        on_change=on_submit,  # Trigger on submission
        disabled=is_processing,  # Disable during processing
    )