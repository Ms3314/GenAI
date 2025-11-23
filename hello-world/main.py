from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()
# System prompt techniques :=> used to make the AI specific to yours own thing
# 1: One shot prompting / Zero Shot Prompting 
# 2: Few Shot Prompting for every input we send a pre defined examples in the system prompts
# 3: Chain of Thought Prompting => basically you re iterate over your solution basically thinking deeply
# 4: Self Consistency prompting => make multiple answers of the thng from 3 models , and then ask from other other models about it , cost badegi magar accuracy badedi
# 5: Persona-based Prompting => kisi ke jaise rehta like an individual (200 lines ke around rehta) 
SYSTEM_PROMPT = """
    You are an helpfull AI assistant who is spec in resolving user queries 
    For the given user input , analyze the input and brak down the problem step by step
    
    the steps are you get the user input , you analyze , you think again and think for several times and then return the output with an simple explanation 

    Follow the steps in sequence such as "analyse" , "think" , "output" , "validate" and finally result 
    
    Example:
    Input: What is 2+2 
    Output: {{"step" : "analyse" , }}
    
"""

# COT project 

# Home Work 
#try (we are orchestrating the AI) multi modal thinking like gemini will be doing the validating and openAI will be be doing the thinking
# anyalyse GEMINI
# thinking OPENAI
# validting Another AI model 

# We are using the ChatML prompting techniques
response = client.responses.create(
    model="gpt-5-nano",
    input=[
        # This is the system prompt which we are giving first 
        {"role":"system" , "content" : SYSTEM_PROMPT},
    ]
)

print(response.output_text)