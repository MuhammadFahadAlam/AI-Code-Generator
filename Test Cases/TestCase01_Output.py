import streamlit as st

# Styling the app with custom CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background: #1e1e1e;
    }
    .sidebar .sidebar-content {
        background: #333333;
    }
    .Widget>label {
        color: #ffffff;
        font-size: 16px;
        padding: 5px 0;
    }
    .css-2trqyj {
        background-color: #333333;
        border: none;
        color: #ffffff;
    }
    .st-bb {
        background-color: transparent;
    }
    .st-at {
        background-color: #555555;
    }
    .st-ae {
        color: #ffffff;
    }
    .st-af {
        color: #009688;
    }
    .st-ag {
        background-color: #333333;
    }
    .st-cj, .st-ck, .st-cd, .st-ce {
        color: #ffffff;
    }
    .st-cm {
        color: #ffffff;
    }
    .file-uploader {
        border: 2px dashed #aaaaaa;
    }
    .file-uploader-label {
        color: #ffffff;
    }
    .st-button>button {
        color: #ffffff;
        background-color: #1976d2;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar settings
st.sidebar.title('Settings')
api_key_placeholder = st.sidebar.empty()
api_key_input = api_key_placeholder.text_input('Enter your API key', type="password")

instructions = """
Instructions:
1. Enter your API key.
2. Use the chat interface to send messages.
3. Upload files if needed.
"""
st.sidebar.markdown(instructions)

# Main chat interface
st.title('Chat Interface')

user_message = st.text_area("Enter your message here", height=100)

file = st.file_uploader("Upload a file", type=['txt','pdf','png','jpg'], accept_multiple_files=False)

if st.button('Send'):
    # You can add functionality here to handle the user message and file
    pass