
# from google import genai

# client = genai.Client(api_key="AQ.Ab8RN6L_La4jMmbkJiiNhsRlGc6wyg--kVTc1XyPrhXvOF6tww")

# for model in client.models.list():
#     print(model.name)



# Import the function to load environment variables from a .env file
from dotenv import load_dotenv

# Import Streamlit for building the web application
import streamlit as st

# Load all environment variables (e.g., GOOGLE_API_KEY) from the .env file
load_dotenv()

# Import the Google Gemini chat model from LangChain
from langchain_google_genai import ChatGoogleGenerativeAI


# Initialize the Gemini language model
# It automatically reads the GOOGLE_API_KEY from the environment
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")

# Display the title of the Streamlit application
st.title("🤖 AskBuddy - AI QnA Bot")

# Display a short description below the title
st.markdown("AskBuddy is an AI-powered QnA bot with Langchain and Google Generative AI.")

# Check whether the chat history exists in the session
# If not, # Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Display all previous messages stored in the session
for message in st.session_state.history:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).markdown(content)


# Create a chat input box where the user can type a question
query = st.chat_input("Ask me anything:")


# Execute only if the user enters a message
# if query:

#     # Save the user's message to the chat history
#     st.session_state.messages.append({"role": "user", "content": query})

#     # Display the user's message immediately
#     st.chat_message("user").markdown(query)

#     # Send the user's query to the Gemini model and get the response
#     res = llm.invoke(query)

#     # Display the AI's response
#     st.chat_message("ai").markdown(res.text)

#     # Save the AI's response to the chat history
#     st.session_state.messages.append({"role": "ai", "content": res.text})


if query:

    # Display user message
    st.chat_message("user").markdown(query)

    # Save user message
    st.session_state.history.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Send complete conversation history to Gemini
    response = llm.invoke(st.session_state.history)

    # Display AI response
    st.chat_message("assistant").markdown(response.content)

    # Save AI response
    st.session_state.history.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )


