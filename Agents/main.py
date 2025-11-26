from openai import OpenAI
from dotenv import load_dotenv
import requests
import os
load_dotenv()

# client = OpenAI()
# we will create an agent which will give us the data 
SEARCH_API_KEY=os.getenv("SEARCH_API_KEY")
# here I will try to make something simiilar to what piyush did

def CallSearchAPI(query):
    url = f"https://www.searchapi.io/api/v1/search?api_key={SEARCH_API_KEY}"
    params = {
    "engine": "google",
    "q": query
    }
    response = requests.get(url, params=params) 
    return response.json()

def GetWhetherData(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = response.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}",
    return "Something went wrong"

def GetUserGithubInfo(username=''):
    #here the github api is hit and his data is extracted 
    url =  f"https://api.github.com/users/{username.lower()}"
    response = requests.get(url)
    {
        
    }
    return response.json() 

data = GetUserGithubInfo("salamusa")
print(data)

SYSTEM_PROMPT = """
    you are an helpfull AI assistant 
"""

# response = client.responses.create(
#     model="gpt-5-nano",
#     input=[
#         {"role":"system" , "content" : SYSTEM_PROMPT} ,
#         {"role":"user" , "content" : "yooo wassup"}
#     ]
# )