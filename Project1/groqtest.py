from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(
    
)
completion = client.chat.completions.create(
    model="moonshotai/kimi-k2-instruct",
    messages=[
      {
        "role": "user",
        "content": "yooo "
      },
      {
        "role": "assistant",
        "content": "Hey there! 👋 What’s up?"
      },
      {
        "role": "user",
        "content": "SOOOO WHAT IS UR MODEL"
      }
    ],
    temperature=0.6,
    max_completion_tokens=4096,
    top_p=1,
    stream=True,
    stop=None
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
