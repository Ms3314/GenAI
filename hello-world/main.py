from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input=[
        {"role":"user" , "content" : "Hey my name is Sami"} ,
        {"role":"assistant" , "content" : "Hello Sami how are you"} ,
        {"role" : "user" , "content" : "What is my name"}
    ]
)

print(response.output_text)