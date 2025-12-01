import json
from prompt import SYSTEM_PROMPT
from methoods import *
# this agent has the ability to ask queries from the users so that it can think and understand user perspective 
# it can take usersGithub account 
# it can also search for information online 


inputvar = [
            {"role":"system" , "content" : SYSTEM_PROMPT},
        ]



def startServer(): 
    while True:
        query = input(">>> ")
        inputvar.append({"role" : "user" , "content" : query})
        while True:
            
            data = openAICall(inputvar)
            print(f"Raw response type: {type(data)}")
            print(f"Raw response: {data[:500]}...")  # Print first 500 chars for debugging
            
            # Strip markdown code blocks if present
            clean_data = data.strip()
            if clean_data.startswith("```json"):
                clean_data = clean_data[7:]  # Remove ```json
            if clean_data.endswith("```"):
                clean_data = clean_data[:-3]  # Remove ```
            clean_data = clean_data.strip()
            
            try:
                propperdata = json.loads(clean_data)
            except json.JSONDecodeError as e:
                print(f"JSON parsing error: {e}")
                print("The AI model returned invalid JSON. This usually happens when:")
                print("1. The content contains unescaped newlines or special characters")
                print("2. The content is too complex for proper JSON formatting")
                print("\nSkipping this response and continuing...")
                continue  # Skip this iteration and ask the model again
                
            # we append the new data now
            inputvar.append({"role" : "assistant" , "content" : data})
            print(f"{propperdata.get('content')}")
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
                print(f"Output 🤖 : {propperdata.get('content')}")
                break
            
startServer()
# data = RunLinuxCommand("npx create-next-app my-next-app")
# print(data)