import streamlit as st
from main import generate_response, encode_uploaded_image
import os


# Initialize chat history if not present in the session state
# This will store all the conversations including the user question and bot's response
# Example: [("User", "What is your name?"), ("Bot", "My name is AI coding assistant."), ...]
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Initialize uploaded file variable
if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None

# Initialize user message variable
if 'user_message' not in st.session_state:
    st.session_state.user_message = ""


# Function to handle the chat
# This function run when the user click the "Send" button
def process_message(user_question, image):
    """
    Here we have implemented the logic to process the message and the file to generate response
    These operations will be performed by this function:
    01- encode_uploaded_image: Encode the image in base64 format to pass it to the model
    02- generate_response: Generate response by using user's question and input image
    03- Store user's question and bot's response to display on the screen 
    """
    
    if image:
        encoded_image = encode_uploaded_image(image)
        chat_response = generate_response(user_question, encoded_image)
    else:
        chat_response = generate_response(user_question)
    
    st.session_state.chat_history.append(("**User**", user_question))
    st.session_state.chat_history.append(("**Bot**", chat_response))


# Function to save openai api key
def save_openai_api_key(api_key):
    """
    Save the api key in the environment variable for model work
    """
    os.environ['OPENAI_API_KEY'] = api_key


def clear_chat_history():
    st.session_state.chat_history = []
    st.session_state.uploaded_file = None
    st.session_state.user_message = ""


# Streamlit App Function
# This function generates the streamlit app and all its UI components
def main():
    """
    Here we have the code to generate the app.
    These are the main operations performed in this function:
    01 - Create sidebar in the application
    02 - Verify and store OpenAI api key entered by the user
    03 - Create chat interface
    04 - Handle click on Send and Clear button
    """

    # Create sidebar in the application
    st.sidebar.title("Settings")
    api_key = st.sidebar.text_input("Enter your API key", type="password")
    st.sidebar.markdown("## Instructions:\n1. Enter your API key.\n2. Use the chat interface to send messages.\n3. Upload files if needed.")

    # Handle openai api key
    if not api_key:
        st.sidebar.warning("Please enter your API key to proceed.")
    else:
        save_openai_api_key(api_key)
        
        # Create Chat Interface in the application
        st.title("Chat Interface")
        
        # Display user question and bot response
        for sender, message in st.session_state.chat_history:
            sender_md = f"**{sender}:**"
            st.markdown(sender_md, unsafe_allow_html=True)
            st.markdown(message, unsafe_allow_html=True)

        # Take question and image input from user
        st.session_state.user_message = st.text_area("Enter your message here", key="message_input", value=st.session_state.user_message)
        st.session_state.uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg'], key="file_uploader")
        
        col1, col2 = st.columns([1, 3])
        
        # Handle button click from user
        if col1.button("Send"):
            if st.session_state.user_message:
                process_message(st.session_state.user_message, st.session_state.uploaded_file)
                st.experimental_rerun()
            else:
                st.error("Please enter a message.")

        with col2:
            if st.button("Clear"):
                clear_chat_history()

if __name__ == "__main__":
    main()
