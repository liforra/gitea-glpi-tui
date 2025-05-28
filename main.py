import requests
import base64
import json
import os

def search(mode:string, ):
    match mode:
        case "serial":
            
    

url = "https://ticket.akademie-awo.de/glpi/apirest.php/initSession"
payload = {}
headers = {
    'Content-Type': 'application/json',
    'App-Token': f'{os.getenv(APP_TOKEN)}',
}
session_token = ''
# The loop is obviously here to keep asking the user for a session token
while not session_token:
    username = input("Please Enter your Username: ")
    password = input("Please Enter your Password: ")
    auth = (username, password)
    verify = input('Verify SSL? y/N')
    remember = input('Remember me? y/N')
    if verify == "y":
        verify = True
    else:
        verify = False
    if remember == "y":
        remember = True
    else:
        remember = False
    response = requests.request("GET", url, headers=headers, data=payload, timeout=5, verify=verify,auth=auth)
    response = str(response.content).strip('b').strip("'") # There is a random "b" at the front and the json data is encapsulated in ' So this gets rid of that
    print(response)
    if response.startswith('{'): # This is a dumb way to check if its json, lets hope it doesnt break
        response = json.loads(response)
        if(response['session_token']): 
            print('Successfully Authenticated.')
            session_token = response['session_token']
        else:
            print('Error: Authentication was not Successful')

print('1 to Search, 2 to Add a computer, 3 to Exit')
option = input()
match option:
    case 1:
        search()
    case 2:
        add('Computer')
    case 3:
        killsession()
        exit()