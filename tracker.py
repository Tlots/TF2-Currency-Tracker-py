# importing
import requests
import colorama
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep

# fixing the colors in the cmd
colorama.init()
reset_color_colorama = colorama.Style.RESET_ALL

webhook = "" # Your discord webhook url
apiKey = "" # Your steam api key
steamID = "" # Your Steam64 ID

webhook_4embed = DiscordWebhook(url=webhook, username="Tracker") # defining the embed for discord
key_count_temp, ref_count_temp, send_message, steam_error_tracker = 0,0, False, 0 # more variable defining

def SteamAPIError(): # checking for any errors in the steam api
    global steam_error_tracker
    print(f"{colorama.Fore.RED}\n[Error]{reset_color_colorama} Steam API status code: {r.status_code}")
    steam_error_tracker += 1
    if steam_error_tracker > 30: # if we get more than 30 steam api errors then send message to discord saying something is wrong
        DiscordWebhook(url= webhook, content= f"[Error] Steam API error. Trying again (Try number: {steam_error_tracker})").execute()
        sleep(15)
    else:
        sleep(5)
print("Made by Tlots \nIf you have any problems Contact me\nDiscord: Tlots#6947\nor report the issue at github: https://github.com/Tlots/TF2-Currency-Tracker-py/issues")

# main
while True:
    r = requests.get(f"http://api.steampowered.com/IEconItems_440/GetPlayerItems/v0001/?key={apiKey}&steamid={steamID}") # getting the backpack of a user

    if r.status_code == 200: # if http code is 200 then proceed
        if r.json()["result"]["status"] == 8 or r.json()["result"]["status"] == 18: # checking if steamid exist
            print(f"{colorama.Fore.RED}[Error]{reset_color_colorama} Invalid SteamID")

        else:
            name = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={apiKey}&steamids={steamID}").json()["response"]["players"][0]["personaname"]
            print(f'{colorama.Fore.YELLOW}​ \nSteamID: {steamID} \nGetting Data For User "{name}"')

            while True: # main loop
                r = requests.get(f"http://api.steampowered.com/IEconItems_440/GetPlayerItems/v0001/?key={apiKey}&steamid={steamID}")
                if r.status_code == 200: # if the site code is OK then proceed
                    r_json = r.json() # converting the site to json file
                    if r_json["result"]["status"] == 1: # if the status code is 1 then proceed
                        key_count, ref_count, scrap_count, rec_count, steam_error_tracker = 0,0,0,0,0 # defining all of the variables
                        HowManyItems = len(r_json["result"]["items"])  # getting the number of items in the inventory
                            
                        for i in range(HowManyItems): # looping through the items to look for keys / metal
                            if r_json["result"]["items"][i]["defindex"] == 5021:    key_count += 1 # 5021 is key index
                            if r_json["result"]["items"][i]["defindex"] == 5000:    scrap_count += 1 # 5000 is scrap index
                            if r_json["result"]["items"][i]["defindex"] == 5001:    rec_count += 1 # 5001 is reclimed metal index
                            if r_json["result"]["items"][i]["defindex"] == 5002:    ref_count += 1 # 5002 is refined metal index

                    
                    # some math
                        scrap_count /= 9 
                        rec_count /= 3
                        ref_count += rec_count + scrap_count
                        ref_float_count = "{:.2f}".format(ref_count) # formating so there will be 2 numbers after the dot (example: 0.00 instead of 0.0000000)
                        ref_float_count_temp = "{:.2f}".format(ref_count_temp) # some more formatting
                        print(colorama.Fore.GREEN) # making the text green inside of the cmd
                        keys_and_ref = f"Keys: {key_count} \nRefined metal: {ref_float_count}" # more formatting
                        print(keys_and_ref) # printing to the cmd the number of keys and metal

                        
                        if ref_count != ref_count_temp or key_count != key_count_temp: # checking if there has been changes
                            if send_message == True:
                                key_difference = int(key_count) - int(key_count_temp)
                                ref_difference = float(ref_float_count) - float(ref_float_count_temp)
                                ref_difference = "{:.2f}".format(ref_difference)
                                if float(ref_difference) > 0:
                                    ref_difference = f"+{ref_difference}"
                                if key_difference > 0:
                                    key_difference = f"+{key_difference}"
                                
                                # sending the embed to discord
                                embed = DiscordEmbed(title=f'{key_count}K | {ref_float_count}R', color='0F5D45')
                                embed.set_author(name=f'Money tracker for user: {name}')
                                embed.add_embed_field(name='​ ', value=f'```Keys: {key_count_temp} ---> {key_count} \nRef: {ref_float_count_temp} ---> {ref_float_count}```')
                                embed.add_embed_field(name='​ ', value=f'```{key_difference} \n{ref_difference}```')
                                webhook_4embed.add_embed(embed)
                                webhook_4embed.execute(remove_embeds=True)

                            ref_count_temp = ref_count
                            key_count_temp = key_count
                            send_message = True

                        sleep(10)

                    if r_json["result"]["status"] == 15:
                        print(f"{colorama.Fore.RED}[Error]{reset_color_colorama} Inventory private")       
                        break

                else:
                    SteamAPIError()
                   

    else:
        SteamAPIError()
