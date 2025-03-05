import streamlit as st
import os
import openai
import subprocess
import base64
from prompts import MESSAGES
import json

ai_client = openai.OpenAI()

def encode_image(file):
    result = base64.b64encode(file.read()).decode("utf-8")
    return result


def initialize_session_state():
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'yaml_editor' not in st.session_state:
        st.session_state.yaml_editor = ""

def add_to_history(role, content):
    st.session_state.chat_history.append((role, content))

def parse_response(response: str) -> tuple[str, str]:
    chat_text = ""
    yaml_code = ""

    print(f"response: \n {response}")
    # response = "\n".join([line for line in response.split("\n") if not line.startswith("`")])

    try:
        response = json.loads(response)
    except json.JSONDecodeError:
        print("Response is not in json format")
        print(response)
        return response, ""
    if 'chat' in response:
        chat_text = response["chat"]
        print(f"chat_text: {chat_text}")
    if "model" in response:
        yaml_code = response["model"]
        #remove lines starting from `
        print(f"yaml_code: {yaml_code}")

    return chat_text, yaml_code

def main():
    st.set_page_config(layout="wide", page_title="Tomato Cookmaster")
    initialize_session_state()

    # Create two main columns
    left_col, right_col = st.columns([1, 3])

    with left_col:
        with st.container(height=700, key="chat_container", border=False):
            # Chat history viewer
            for author, message in st.session_state.chat_history:
                with st.chat_message(author):
                    st.markdown(message)

        with st.container(height= 100, key="chat_input", border=False):

            if prompt := st.chat_input("How can I help you today?", accept_file=True):
                file = prompt["files"][0] if len(prompt["files"]) else None
                prompt = prompt["text"]

                add_to_history("user", prompt)
                messages = MESSAGES + [{"role": "developer", "content": f"This is the current model:\n{st.session_state.yaml_editor}"}]
                messages = messages + [{"role": "user", "content": prompt}]
                if file:
                    messages = messages + [{
                        "role": "user", "content": [
                            {
                                "type": "image_url", 
                                "image_url": {"url": f"data:image/jpeg;base64,{encode_image(file)}"},
                            }
                        ]
                    }]

                completion = ai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages
                )
                response = completion.choices[0].message.content

                chat_text, yaml_code = parse_response(response)
                
                if yaml_code:
                    st.session_state.yaml_editor = yaml_code
                
                add_to_history("ai", chat_text)
                messages = MESSAGES + [{"role": "assistant", "content": response}]

                st.rerun()

    with right_col:
        st.code(st.session_state.yaml_editor, line_numbers=True, language='yaml', height=750, )

if __name__ == "__main__":
    main()
