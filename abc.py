# libraries: streamlit; google-generativeai; python-dotenv
#install gtts & playsound==1.2.2
import time
import gtts
import playsound

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from PIL import Image
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load gemini pro model and get response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
  response = chat.send_message(question, stream=True)
  return response

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.title("EDU BOT")

# Input field and submit button
input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the question")

# Process user input
if submit_button and input_text:
  response = get_gemini_response(input_text)

  # Store the output text in a variable
  output_text = " "
  for chunk in response:
    output_text += chunk.text

  # Display response
  st.subheader("The response is:")
  st.write(output_text)

sound=gtts.gTTS(output_text, lang="en") #language set as english
sound.save("abc_proj.mp3")


playsound.playsound("abc_proj.mp3")
# deleting audio file once executed
file_path = "D:\project_py\Project\abc_proj.mp3"

if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted successfully.")
else:
    print(f"{file_path} does not exist.")