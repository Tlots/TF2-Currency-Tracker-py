# TF2-Currency-Tracker-py
Track your keys / ref all in your discord server!  
Basically this code tracks changes that are made in your tf2 keys / metal using requests library and steam api then sends the changes to your discord server using python and discord-webhook module.


# PREVIEW:
![image](https://user-images.githubusercontent.com/51534102/142774711-89e6e486-39bb-4c5e-8562-e2ae00ae4a10.png)
![image](https://user-images.githubusercontent.com/51534102/142774257-051fe165-7d1d-45d4-b3b0-b16e257e4b44.png)




# What you will need:  
• Python 3.9+ (Add python to PATH)  
• Download the repository as zip  
![image](https://user-images.githubusercontent.com/51534102/142775472-13bc4769-ff19-4e26-8212-43377b74e200.png)  
Download the required modules (type all of that inside cmd):  
• pip install requests  
• pip install discord-webhook  
• pip install colorama  
or if you want to skip all of that just go to the folder in cmd and use "pip install -r requirements.txt"

# What Do I Do Now? SETUP
After you have installed everything you will need to change these lines (Open the py file with text editor):  
```
webhook = "" # Your discord webhook url
apiKey = "" # Your steam api key
steamID = "" # Your Steam64 ID
```
• How to get discord webhook url: create a discord server -> go to the channel settings -> integrations -> view webhooks -> new webhook -> copy webhook url  

• How to get steam api key: Go here: https://steamcommunity.com/dev/apikey -> what I wrote in the domain name is: "127.0.0.1" and it worked  

• How to get steam64 ID: Go to steam id finder: https://steamid.xyz and put your steam url profile there  

**EXAMPLE:**
```
webhook = "https://discord.com/api/webhooks/91205715274891/sC2QoRhAeKKZhBPtFiRCghEf45vSRUoB2nh5f7xPV6ZAHJp" # Your discord webhook url
apiKey = "4D5FS7FA497GAS289YG89A7T" # Your steam api key
steamID = "76561198285260753" # Your Steam64 ID
```
Now save the file and double click it (double click tracker.py)

**Common sense: The program will work as long as you're running it**  
**To run the code consistently you can use https://pythonanywhere.com**


# Known Errors:  
• **Pretty common one**: Steam API 503 HTTP Code - This error happens because the web server is currently unable to handle the HTTP request due to a temporary overloading or maintenance of the server.  

• Webhook sends separate messages about the same trade (I might fix this later):       
![image](https://user-images.githubusercontent.com/51534102/142773946-7f16bbd0-ae57-45c6-84ba-65863d844301.png)  

• Looks weird on mobile:  
![image](https://user-images.githubusercontent.com/51534102/142775051-7c66aa1a-8cf7-4055-962a-567ce8200ba2.png)
