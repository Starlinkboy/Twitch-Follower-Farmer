# Twitch Follower Farmer
# Alt Account Suggested
# Speed: 5-15 followers per minute
# ❕❕ Account on which you want the bot to run must be in this server : discord.gg/xtwitch ❕❕
# Made By Starlinkboy #0159
# Made with Love ❌ Code ✅

import discord
from discord.ext import tasks
from pystyle import Colorate, Colors


starlink = """
                 
                 
███████╗████████╗ █████╗ ██████╗ ██╗     ██╗███╗   ██╗██╗  ██╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║     ██║████╗  ██║██║ ██╔╝
███████╗   ██║   ███████║██████╔╝██║     ██║██╔██╗ ██║█████╔╝ 
╚════██║   ██║   ██╔══██║██╔══██╗██║     ██║██║╚██╗██║██╔═██╗ 
███████║   ██║   ██║  ██║██║  ██║███████╗██║██║ ╚████║██║  ██╗
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
                                                              


                                           """


print(Colorate.Horizontal(Colors.red_to_black, (starlink)))
TOKEN = input(Colorate.Horizontal(Colors.red_to_black,"Account Token: "))
token = (TOKEN)

client = discord.Client()

@tasks.loop(minutes=1)
async def test():
    
    channel = client.get_channel(997521861783068812)
    await channel.send(f".tfollow starlinkboy")
    print(Colorate.Horizontal(Colors.red_to_black, "Message Sent!"))
    
@client.event
async def on_ready():
    test.start()

client.run(token, bot=False)