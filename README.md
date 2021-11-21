# TF2-Currency-Tracker-py
Track your keys / ref all in your discord server!  
Basically this code tracks changes in your tf2 keys / metal using requests library and steam api then sends the changes to your discord server using python and discord-webhook module.

# PREVIEW:
![image](https://user-images.githubusercontent.com/51534102/142774711-89e6e486-39bb-4c5e-8562-e2ae00ae4a10.png)
![image](https://user-images.githubusercontent.com/51534102/142774257-051fe165-7d1d-45d4-b3b0-b16e257e4b44.png)



# What you will need:  
Python 3.9+ (Add python to PATH)
Download the repository as zip
type all of that inside cmd:  
• pip install requests  
• pip install discord-webhook  
• pip install colorama  
or if you want to skip all of that just go to the folder in cmd and use "pip install -r requests.txt"

# What to do 101
After you installed everything
```
webhook = "" # Your discord webhook url
apiKey = "" # Your steam api key
steamID = "" # Your Steam64 ID
```

# Common Errors:  
• Steam API 503 HTTP Code - This error happens because the web server is currently unable to handle the HTTP request due to a temporary overloading or maintenance of the server.  

• Webhook sends separate messages about the same trade (I might fix this later):       
![image](https://user-images.githubusercontent.com/51534102/142773946-7f16bbd0-ae57-45c6-84ba-65863d844301.png)  

• Looks weird on mobile:  
![image](https://user-images.githubusercontent.com/51534102/142775051-7c66aa1a-8cf7-4055-962a-567ce8200ba2.png)
