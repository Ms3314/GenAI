from openai import OpenAI
from dotenv import load_dotenv
import requests
import subprocess
import os
load_dotenv()
import json
from prompt import SYSTEM_PROMPT

# this agent has the ability to ask queries from the users so that it can think and understand user perspective 
# it can take usersGithub account 
# it can also search for information online 


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
    output = subprocess.check_output("ls", shell=True, text=True)
    return output


def geminiAPICall(input):
    print("we need to do a gemini api call here")
    
def grokAPICall(input):
    print("we will be doing a groq api call here ")
 
 
def openAICall(input):
    data = client.responses.create(
        model="gpt-5-mini",
        input=inputvar
    )
    return data.output_text
    
 
inputvar = [
            {"role":"system" , "content" : SYSTEM_PROMPT},
        ]
 
while True:
    query = input(">>> ")
    inputvar.append({"role" : "user" , "content" : query})
    while True:
        
        data = openAICall(inputvar)
        print(type(data))
        print(data)
        propperdata = json.loads(data)  
        # we append the new data now
        inputvar.append({"role" : "assistant" , "content" : data})
        print(f"{propperdata.get("step")} : {propperdata}")
        
        
        # the tool call interface

        if propperdata.get("step") == "toolcall":
            if propperdata.get("tool") == "GetGithubAccountInformation":
                result = GetUserGithubInfo(propperdata.get("content"))
                inputvar.append({"role":"assistant" , "content" : json.dumps(result)})
                print("we will get the github info")
            if propperdata.get("tool") == "SearchWeb":
                print("You will be able to search the web now")
                result = CallSearchAPI(propperdata.get("content"))
                inputvar.append({"role" : "assistant" , "content" : json.dumps(result)})
            if propperdata.get("tool") == "RunLinuxCommand":
                print("You will be able to run any linux command")
                result = RunLinuxCommand(propperdata.get("content"))
                inputvar.append({"role" : "assistant" , "content" : json.dumps(result)})
            if propperdata.get("tool") == "GetWhetherData":
                # CITY NAME is supposed to be passed here 
                result = GetWhetherData(propperdata.get("content"))
                inputvar.append({"role":"assistant" , "content" : json.dumps(result)})
                
        if propperdata.get("step") == "result":
            print(f"Output 🤖 : {propperdata.get("content")}")
            break
        