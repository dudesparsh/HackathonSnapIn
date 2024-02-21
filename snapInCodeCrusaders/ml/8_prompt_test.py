

## Before pushing keep in mind to remove the env key and org

import os
os.environ["openai_api_key"] = ""
os.environ["openai_organization"] = ""

from langchain import PromptTemplate

demo_template='''I want you to act as a acting financial advisor for people.
In an easy way, explain the basics of {financial_concept}.'''

prompt=PromptTemplate(
    input_variables=['financial_concept'],
    template=demo_template
    )

prompt.format(financial_concept='income tax')

from langchain.llms import OpenAI
from langchain.chains import LLMChain

llm=OpenAI(temperature=0.7)
chain1=LLMChain(llm=llm,prompt=prompt)

print(chain1.run('GDP'))

# llm = OpenAI(openai_api_key=openai_api_key, openai_organization=openai_api_key, temperature=0.9)  # model_name="text-davinci-003"
