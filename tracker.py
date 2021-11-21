import requests
import colorama
from discord_webhook import DiscordWebhook, DiscordEmbed
from time import sleep


colorama.init()
reset_color_colorama = colorama.Style.RESET_ALL

webhook = "" # Your discord webhook url
apiKey = "" # Your steam api key
steamID = "" # Your Steam64 ID

webhook_4embed = DiscordWebhook(url=webhook, username="Tracker")
key_count_temp, ref_count_temp, send_message, steam_error_tracker = 0,0, False, 0

def SteamAPIError():
    global steam_error_tracker
    print(f"{colorama.Fore.RED}\n[Error]{reset_color_colorama} Steam API status code: {r.status_code}")
    steam_error_tracker += 1
    if steam_error_tracker > 30:
        DiscordWebhook(url= webhook, content= f"[Error] Steam API error. Trying again (Try number: {steam_error_tracker})").execute()
    sleep(5)



while True:
    r = requests.get(f"http://api.steampowered.com/IEconItems_440/GetPlayerItems/v0001/?key={apiKey}&steamid={steamID}")
    if r.status_code == 200:
        if r.json()["result"]["status"] == 8 or r.json()["result"]["status"] == 18:
            print(f"{colorama.Fore.RED}[Error]{reset_color_colorama} Invalid SteamID")

        else:
            name = requests.get(f"https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v2/?key={apiKey}&steamids={steamID}").json()["response"]["players"][0]["personaname"]
            print(f'{colorama.Fore.YELLOW}​ \nSteamID: {steamID} \nGetting Data For User "{name}"')

            while True:
                r = requests.get(f"http://api.steampowered.com/IEconItems_440/GetPlayerItems/v0001/?key={apiKey}&steamid={steamID}")

                if r.status_code == 200:
                    r_json = r.json()
                    if r_json["result"]["status"] == 1:
                        key_count, ref_count, scrap_count, rec_count, steam_error_tracker = 0,0,0,0,0
                        HowManyItems = len(r_json["result"]["items"])
                            
                        for i in range(HowManyItems):
                            if r_json["result"]["items"][i]["defindex"] == 5021:    key_count += 1
                            if r_json["result"]["items"][i]["defindex"] == 5000:    scrap_count += 1
                            if r_json["result"]["items"][i]["defindex"] == 5001:    rec_count += 1
                            if r_json["result"]["items"][i]["defindex"] == 5002:    ref_count += 1


                        scrap_count /= 9
                        rec_count /= 3
                        ref_count += rec_count + scrap_count
                        ref_float_count = "{:.2f}".format(ref_count)
                        ref_float_count_temp = "{:.2f}".format(ref_count_temp)
                        print(colorama.Fore.GREEN)
                        keys_and_ref = f"Keys: {key_count} \nRefined metal: {ref_float_count}"
                        print(keys_and_ref)

                        if ref_count != ref_count_temp or key_count != key_count_temp:
                            if send_message == True:
                                key_difference = int(key_count) - int(key_count_temp)
                                ref_difference = float(ref_float_count) - float(ref_float_count_temp)
                                ref_difference = "{:.2f}".format(ref_difference)
                                if float(ref_difference) > 0:
                                    ref_difference = f"+{ref_difference}"
                                if key_difference > 0:
                                    key_difference = f"+{key_difference}"

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
