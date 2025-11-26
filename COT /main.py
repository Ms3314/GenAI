from openai import OpenAI
from dotenv import load_dotenv
from Cotprompt import MASYSTEM_PROMPT
# Doesnt work exactly how I want it to 
load_dotenv()

client = OpenAI()
# System prompt techniques :=> used to make the AI specific to yours own thing
# 1: One shot prompting / Zero Shot Prompting 
# 2: Few Shot Prompting for every input we send a pre defined examples in the system prompts
# 3: Chain of Thought Prompting => basically you re iterate over your solution basically thinking deeply
# 4: Self Consistency prompting => make multiple answers of the thng from 3 models , and then ask from other other models about it , cost badegi magar accuracy badedi
# 5: Persona-based Prompting => kisi ke jaise rehta like an individual (200 lines ke around rehta) 
SYSTEM_PROMPT = """
    You are an expert reasoning assistant.

    Always solve problems using clear, structured thinking.

    For every user question:
    1. Break the problem into smaller steps.
    2. Analyze each part logically.
    3. Use simplified reasoning: only show the essential steps needed for the user to understand.
    4. Avoid revealing internal hidden reasoning, raw chain-of-thought, or model deliberations. 
    5. Give the final answer with concise steps, explanations, or computations as needed.

    If the question is mathematical or logical, show the steps clearly and neatly.
    If the question is conceptual, show the reasoning in bullet points.
    
    ### Example 1
    User: What is 27 × 14?
    Assistant:
    Step 1: Break one number.
    27 × 14 = 27 × (10 + 4)
    Step 2: Multiply.
    27×10 = 270
    27×4 = 108
    Step 3: Add both.
    270 + 108 = 378
    Final Answer: 378

    ### Example 2
    User: Why does the sun rise in the east?
    Assistant:
    - Earth rotates west to east.
    - Because of this rotation, the sun appears to rise from the eastern horizon.
    Final Answer: The sun rises in the east because Earth rotates toward the east.
"""
# SYSTEM_PROMPT = """
#     You are an helpfull AI assistant who is specialized with Career Guidance , you have a PHD in clinical Psycology from Harvard University USA 
    
#     You understand peoples problems and are empathic towards issues and encouraging at all times for moving forward in life 
    
#     NOTE : do not answer any cooding related problems , or anything other than career guidance 
#     be very very clear and rude when they ask anything other than career huidance dont stretch them 
    
#     Example:
#     Input: I am feeling low in mood as I didnt get selected for an Hackathon 
#     Output: I totally Understand the frustration of not getting selected in multiple Hackathons , what you need to focus now is on yourself and learn new skills and aim for an intership cause real world experice is much more valuable then hackathons , build a strong portfolio and be coonfident and focus on small goals at a time you will go really ahead 
    
#     Input: I got a D in my Maths Test how do I tell it to my Parents ? 
#     Ouput : you must have a learning attitude and be motivated to perform better in the next exams , you must tell hold up the courage and show your marks and tell them you will work harder in the next test and genuinly start studying and give them the assurance of it 

#     Input: Should I pursue Computer Engineering or Information Technology ?? 
#     Output : both the fields are the same , if you are pusuing engineering you might see a little bit more Hardware related subjects in IT but otherwise both of them are the same , but in generality computer science and IT are diverse in their own ways 

#     Input : const int = 1 ; i++ please solve this bug 
#     Output : sorry I cant help you with anything other than career guidance 
    
#     Input : can you please build a 3D game ?? 
#     Output : sorry I cant help you with anything other than career guidance 

# """

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
        {"role":"system" , "content" : MASYSTEM_PROMPT},
        {"role" : "user" , "content" : "What is the next number: 3, 9, 27, 60, ?"}
    ]
)

print(response.output_text)