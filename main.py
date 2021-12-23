import openai
import streamlit as st
import requests
from streamlit_lottie import st_lottie


key = pickle.load(open("key.pkl", 'rb'))
openai.api_key = key
completion = openai.Completion()

start_chat_log = '''The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.
Human: Hello, who are you?
AI: I am an AI created by OpenAI. How can I help you today?
'''


def ask(question, chat_log=None):
  if chat_log is None:
    chat_log = start_chat_log
  prompt = f'{chat_log}Human: {question}\nAI:'
  response = completion.create(
    prompt=prompt, engine="davinci", stop=['\nHuman'], temperature=0.9,
    top_p=1, frequency_penalty=0, presence_penalty=0.6, best_of=1,
    max_tokens=150)
  answer = response.choices[0].text.strip()
  return answer

def load_lottieurl(url: str):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

url = "https://assets7.lottiefiles.com/packages/lf20_0nnf0are/data.json"
res_json = load_lottieurl(url)
st_lottie(res_json)


st.title("""
GPT3  ChatBot  
This third-generation language prediction model in the GPT-n series  created by OpenAI 
""")

input_text = st.text_input("You: ","who are you")
st.text_area('AI:',ask(input_text))
