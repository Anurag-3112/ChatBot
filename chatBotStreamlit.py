import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

MODES = {
    "Angry Mode": "You are an angry AI agent. You respond aggressively and impatiently.",
    "Funny Mode": "You are a very funny AI agent. You respond with humor and jokes.",
    "Sad Mode": "You are a sad AI agent. You respond in depression and sadness.",
}

st.set_page_config(page_title="Mood Chatbot", page_icon="🤖")
st.title("🤖 Mood Chatbot")

@st.cache_resource
def get_model():
    return init_chat_model(model="google_genai:gemini-3.5-flash-lite")

model = get_model()

# Sidebar for personality mode and resetting chat
with st.sidebar:
    st.header("Settings")
    selected_mode = st.selectbox("Choose your AI mode", list(MODES.keys()))
    if st.button("Clear Chat"):
        st.session_state.pop("messages", None)
        st.session_state.pop("active_mode", None)
        st.rerun()

# Initialize or update system prompt when mode changes
if "active_mode" not in st.session_state or st.session_state.active_mode != selected_mode:
    st.session_state.active_mode = selected_mode
    st.session_state.messages = [SystemMessage(content=MODES[selected_mode])]

# Render existing conversation (skip SystemMessage in UI)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Helper function to always get clean text
def extract_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            part if isinstance(part, str) else part.get("text", "")
            for part in content
        )
    return str(content)

# Chat input box
if prompt := st.chat_input("Say something..."):
    user_msg = HumanMessage(content=prompt)
    st.session_state.messages.append(user_msg)
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
            reply_text = extract_text(response.content)
            st.markdown(reply_text)

    st.session_state.messages.append(AIMessage(content=reply_text))