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
import statistics
from statistics import multimode
from time import sleep

load_dotenv()
client = discord.Client()


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
    roleIdGloom = 931329921190608927 #gloom role id 931329921190608927
    role = message.guild.get_role(roleIdGloom)
    listFor = []
   
    if message.channel.id == gloomChannel and message.author != client.user:
        # check word if match with the list
        if any(word in msg_content for word in marlyWord) and role not in message.author.roles: 
            await message.channel.send('Bad Marly! Leave them to play GloomHaven')
            await message.delete(delay =3)
        
        #Change 'Marlys' comments to random upper lower cased
        elif any(word in msg_content for word in marlyWord) and role not in message.author.roles:
            await message.channel.send(''.join([char.lower() if random.randint(0,1) else char.upper() \
                      for char in message.content]))
            await message.delete(delay =3)

        #Add up?
        elif any(word in msg_content for word in marlyWord) and role in message.author.roles:
            message.content += listFor
            sleep (5)
            await message.channel.send('The most common answer is % s' %(multimode(listFor)))
            listFor.clear()

client.run(os.getenv('TOKEN'))