from openai import openAI

client = openAI()


response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=input
    )