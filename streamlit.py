# import streamlit as st
# import google.generativeai as genai

# # Configure Gemini API
# genai.configure(api_key="")

# model = genai.GenerativeModel('gemini-2.0-flash') # or 'gemini-2.0-pro'

# # Initialize chat history
# if "memory" not in st.session_state:
#     st.session_state.memory = []

# # Title
# st.title("🤱 Mom Friend Chatbot")

# # Input form
# with st.form("chat_form", clear_on_submit=True):
#     user_input = st.text_input("You:", placeholder="Ask me anything about pregnancy...")
#     submit = st.form_submit_button("Send")

# # Handle input
# if submit and user_input:
#     st.session_state.memory.append(f"User: {user_input}")

#     prompt = (
#         "You are a supportive, loving, slightly humorous 'Mom Friend' for a pregnant woman. "
#         "You talk like a real mom would — warm, honest, and emotionally supportive. "
#         "Keep your answers short, sweet, and helpful.\n\n"
#         + "\n".join(st.session_state.memory) +
#         "\nAI:"
#     )

#     response = model.generate_content(prompt)
#     ai_reply = response.text.strip()

#     st.session_state.memory.append(f"AI: {ai_reply}")

# # Display chat history
# for msg in st.session_state.memory:
#     if msg.startswith("User:"):
#         st.markdown(f"**👩 You:** {msg[6:]}")
#     elif msg.startswith("AI:"):
#         st.markdown(f"**🤱 Mom Friend:** {msg[4:]}")




# ??//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



# import streamlit as st
# from google import genai

# # Configure Gemini API
# client = genai.Client(
#     api_key="AIzaSyBQNVfFReFZps2nLZWzq5zxL9B8Zxhqr7I"
# )

# # Initialize chat history
# if "memory" not in st.session_state:
#     st.session_state.memory = []

# # Title
# st.title("🤱 Mom Friend Chatbot")

# # Input form
# with st.form("chat_form", clear_on_submit=True):
#     user_input = st.text_input(
#         "You:",
#         placeholder="Ask me anything about pregnancy..."
#     )
#     submit = st.form_submit_button("Send")

# # Handle input
# if submit and user_input:
#     st.session_state.memory.append(
#         f"User: {user_input}"
#     )

#     prompt = (
#         "You are a supportive, loving, slightly humorous "
#         "'Mom Friend' for a pregnant woman. "
#         "You talk like a real mom would — warm, honest, "
#         "and emotionally supportive. "
#         "Keep your answers short, sweet, and helpful.\n\n"
#         + "\n".join(st.session_state.memory)
#         + "\nAI:"
#     )

#     response = client.models.generate_content(
#         model="gemini-3.8-flash",
#         contents=prompt
#     )

#     ai_reply = response.text.strip()

#     st.session_state.memory.append(
#         f"AI: {ai_reply}"
#     )

# # Display chat history
# for msg in st.session_state.memory:
#     if msg.startswith("User:"):
#         st.markdown(f"**👩 You:** {msg[6:]}")
#     elif msg.startswith("AI:"):
#         st.markdown(f"**🤱 Mom Friend:** {msg[4:]}")





# //////////////////////////////


import os
import streamlit as st
from google import genai


# Gemini client
client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)


# Initialize chat history
if "memory" not in st.session_state:
    st.session_state.memory = []


st.title("🤱 Mom Friend Chatbot")


with st.form("chat_form", clear_on_submit=True):

    user_input = st.text_input(
        "You:",
        placeholder="Ask me anything about pregnancy..."
    )

    submit = st.form_submit_button("Send")


if submit and user_input:

    st.session_state.memory.append(
        f"User: {user_input}"
    )

    prompt = (
        "You are a supportive, loving, slightly humorous "
        "'Mom Friend' for a pregnant woman. "
        "You talk like a real mom would — warm, honest, "
        "and emotionally supportive. "
        "Keep your answers short, sweet, and helpful.\n\n"
        + "\n".join(st.session_state.memory)
        + "\nAI:"
    )

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    ai_reply = response.text.strip()

    st.session_state.memory.append(
        f"AI: {ai_reply}"
    )


for msg in st.session_state.memory:

    if msg.startswith("User:"):
        st.markdown(
            f"**👩 You:** {msg[6:]}"
        )

    elif msg.startswith("AI:"):
        st.markdown(
            f"**🤱 Mom Friend:** {msg[4:]}"
        )