import streamlit as st
import ollama

# Page Configuration
st.set_page_config(page_title="PrivaChat - Local AI", page_icon="🔒", layout="centered")

st.title("🔒 PrivaChat")
st.markdown("A private, 100% offline chatbot powered by Ollama running locally on your machine.")

# Initialize Session State for Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar Configuration
with st.sidebar:
    st.header("Settings")

    # Fetch available models from Ollama
    try:
        # We use a short timeout or simple check to avoid hanging the UI
        models_info = ollama.list()
        # Extract model names from the response
        # Depending on ollama version, models_info might be a list or a dict with 'models' key
        if isinstance(models_info, dict):
            model_list = [m['name'] for m in models_info.get('models', [])]
        elif isinstance(models_info, list):
            model_list = [m['name'] for m in models_info]
        else:
            model_list = []

        if not model_list:
            model_list = ["gemma3:1b", "llama3", "mistral"]
    except Exception:
        # Silently fall back to defaults instead of showing an error box
        model_list = ["gemma3:1b", "llama3", "mistral"]

    selected_model = st.selectbox(
        "Choose a model",
        options=model_list,
        index=0 if model_list else None,
        help="Select the local model you want to use for this conversation."
    )

    st.divider()

    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Assistant Response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""

        try:
            # Call Ollama with streaming enabled
            stream = ollama.chat(
                model=selected_model,
                messages=st.session_state.messages,
                stream=True,
            )

            # Stream the response to the UI
            for chunk in stream:
                content = chunk['message']['content']
                full_response += content
                response_placeholder.markdown(full_response + "▌")

            # Final update to remove the cursor
            response_placeholder.markdown(full_response)

            # Save assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
