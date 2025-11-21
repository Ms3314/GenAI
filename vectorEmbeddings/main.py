from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()

client = OpenAI()
text = "dog chases cat"

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="text"
)

# this is giving me all the embeddings properly 
data = response.data[0].embedding
data1 = len(data)
print(data)
print(data1)