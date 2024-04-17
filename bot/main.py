import discord
from discord import app_commands

from json import loads, dump
from os import _exit, system
from time import sleep
from colorama import Fore

try:
    from lib.createKeys import createKey
    from lib.deleteKeys import deleteKey
    from lib.verifyKeys import verifyKey
    from lib.getKeys import getKey
except Exception as e:
    print(f"Wrong file or Import Error!\nExitting!\n{e}")
    sleep(1)
    _exit(0)

class config:
    def __init__(self) -> None:
        try:
            self.__config__ = loads(open("config/config.json", "r+").read())
            if self.__config__ is None or self.__config__ == "":
                self.createConfig()
        except Exception as e:
            try:
                print(f"Unable to read config! Creating config!\n{e}")
                self.createConfig()
                self.__config__ = loads(open("config/config.json", "r+").read())
            except Exception as e:
                print(f"Config creation failed!\n{e}")
                _exit(0)

    def createConfig(self):
        with open("config/config.json", "w") as outfile:
                    dump(
                    {
                        "accessKey": "puturauthkey",
                        "url": "http://127.0.0.1:85/",
                        "projectName": "k4rb1ne"
                    }, outfile)

def clear() -> None:
    system("cls")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

config = config()
accessKey: str = config.__config__['accessKey']
url: str = config.__config__['url']
projectName: str = config.__config__['projectName']
token: str = config.__config__['token']

# create instance of class
#createKey = createKey(accessKey, url, projectName)
#deleteKey = deleteKey(accessKey, url, projectName)
verifyKey = verifyKey(accessKey, url, projectName)
getKey = getKey(accessKey, url, projectName)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Use /token to generate a token!"))
    print(f'{Fore.MAGENTA}\tStarted!\n')
    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@tree.command(
    name="create",
    description="Generate a K4RB1NE Token"
)
@app_commands.describe(
    id = "Discord ID:",
    duration = "Duration:"
)
async def CreateToken(interaction: discord.Interaction, id: str, duration: str):
    if interaction.user.id == "1088919697807904780":
        print("Used by nextrix")
        genKey = createKey(accessKey, url, projectName, id, duration)
    else:
        print(f"Used by {interaction.user.id} lmao")
        pass
    embed=discord.Embed(title="Token Generator", description="Generated Token", color=0xff0000)
    embed.set_author(name="by nextrixvfx", url="https://nextrix.xyz/", icon_url="")
    #embed.set_thumbnail(url="")
    time = ""
    if duration == "1":
        time = "1 Day"
    elif duration == "2":
        time = "1 Week"
    elif duration == "3":
        time = "1 Month"
    elif duration == "4":
        time = "3 Months"
    elif duration == "5" or duration == "-1":
        time = "Life"
    else:
        time = f"Not Valid: {duration}"
    embed.add_field(name="ID: ", value=f"{id}", inline=True)
    embed.add_field(name="Token: ", value=f"{genKey.create()}", inline=True)
    embed.add_field(name="Duration:" , value=f"{time}", inline=True)
    embed.set_footer(text="K4RB1NE.AI 2024")
    
    print("Recieved!")
    await interaction.response.send_message(embed=embed)

@tree.command(
    name="delete",
    description=f"Delete a K4RB1NE Token"
)
@app_commands.describe(
    id = "Discord ID:"
)
async def DeleteToken(interaction: discord.Interaction, id: str):
    delKey = deleteKey(accessKey, url, projectName, id)
    delKey.delete()

    embed=discord.Embed(title="Token Generator", description="Deleted Token", color=0xff0000)
    embed.set_author(name="by nextrixvfx", url="https://nextrix.xyz/", icon_url="")
    #embed.set_thumbnail(url="")
    embed.add_field(name="ID: ", value=f"{id}", inline=True)
    embed.set_footer(text="K4RB1NE.AI 2024")
    
    print("Recieved!")
    await interaction.response.send_message(embed=embed)

if __name__ == "__main__":
    try:
        clear()
        client.run(token)
    except Exception as e:
        print(f"Error: {e}")