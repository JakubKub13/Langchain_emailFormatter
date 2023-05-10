import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    Below is an email that may be poorly worded.
    Your goal is to:
    - Properly format the email
    - Convert the input text to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples of different tones:
    - Formal: We went to Barcelona for the weekend. We have a lot of things to tell.
    - Informal: Went to Barcelona for the weekend. Got lots to tell you.

    Here are some examples of different dialects:
    - American: French Fires, cotton candy, apartment, garbage, cookie, sneakers
    - British: chips, candy floss, flag, rubbish, biscuit, green fingers

    Below is the email, tone and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    EMAIL: {email}

    YOUR RESPONSE:
"""
OPENAI_API_KEY="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"

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template,
)

def load_LLM():
    """Logic for loading the chain you want to use goes here"""
    llm = OpenAI(temperature=0.5, openai_api_key=OPENAI_API_KEY)
    return llm

llm = load_LLM()

st.set_page_config(page_title="Globalize Email", page_icon=":robot:")
st.header("Globalize Email")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Professionals ofter would like to improve their email writing skills. This app will help you to write better emails.")
                         
with col2:
    st.image(image='mail.png', width=250, caption='mail')

st.markdown("## Enter your email to convert below")

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'Which tone would you like to use?',
        ('Formal', 'Informal'))
   
with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like to use?',
        ('American', 'British'))


def get_text():
    input_text = st.text_area(label="", placeholder="Your email....", key="email_input")
    return input_text

email_input = get_text()

st.markdown("## Your converted email:")

if email_input:
    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)

    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)