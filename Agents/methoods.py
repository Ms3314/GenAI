from openai import OpenAI
from dotenv import load_dotenv
import requests
import subprocess
import os
load_dotenv()

client = OpenAI()
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
    calldata =  response.json()
    # the search results data is given in priorities 
    print("We have returned something lol")
    return {
        "p1" : calldata.get("organic_results")[0] ,
        "p2" : calldata.get("organic_results")[1] ,
        "p3" : calldata.get("organic_results")[3]
    }

def GetWhetherData(city):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}",
    return "Something went wrong"

def GetUserGithubInfo(username=''):
    #here the github api is hit and his data is extracted 
    url =  f"https://api.github.com/users/{username.lower()}"
    response = requests.get(url)
    dataFromGithubAPI = {
        username : "etc"
        # etc etc etc
    }
    return response.json() 


def RunLinuxCommand(command):
    # using the sub process instead of os library so that I can store the output of the command that has been run by the model
    print("------------------------------------------------")
    print(f"what command u want to run {command}")
    print("Linux command run")
    try:
        # output = subprocess.run(command, shell=True, capture_output=True, text=True)
        output = os.system(command)
        print(output)
        return {
            "stdout": output.stdout,
            "stderr": output.stderr,
            "returncode": output.returncode,
            "success": output.returncode == 0
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "returncode": -1,
            "success": False
        }


def geminiAPICall(input):
    print("we need to do a gemini api call here")
    
def grokAPICall(input):
    print("we will be doing a groq api call here ")
 
 
def openAICall(input):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=input
    )
    return response.choices[0].message.content
    