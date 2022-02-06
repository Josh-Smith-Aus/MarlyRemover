## Set up for DigitalOcean
# Build Command
#    -->   pip install -r requirements.txt 
#  Run Command
#    -->   python main.py
# 
# Run:
#    pip3 freeze > requirements.txt
#in terminal here to create requirements.txt file
#
#



import discord
import os
import random
from discord import channel
from dotenv import load_dotenv
load_dotenv()
client = discord.Client()
import os


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    
    if message.author == client.user:
        await message.delete(delay =5)

    gloomChannel = 928503396107972639 #channel.id for gloomhaven 928503396107972639   
    msg_content = message.content.lower()
    marlyWord = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
    Marly = 332674954958995466 #Marlys user ID = 332674954958995466
    RoleIdGloom = 928262721550565417 #gloom role id
    


    # check word if match with the list
    if any(word in msg_content for word in marlyWord) and message.author.id not in RoleIdGloom and message.channel.id == gloomChannel:
        await message.channel.send('Bad Marly! Leave them to play GloomHaven')
        await message.delete(delay =3)
    elif not all(word in msg_content for word in marlyWord) and message.author.id not in RoleIdGloom and message.channel.id == gloomChannel:
        #Change Marlys comments to random upper lower case
        await message.channel.send(''.join([char.lower() if random.randint(0,1) else char.upper() \
                   for char in message.content]))
        await message.delete(delay =3)


client.run(os.getenv('TOKEN'))