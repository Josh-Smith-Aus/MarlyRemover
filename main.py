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
        await message.delete(delay =3)

    gloomChannel = 928882150995025961 #channel.id for gloomhaven    
    msg_content = message.content.lower()
    marlyWord = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',]
    Marly = 305289523619692544 #Marlys user ID = 332674954958995466, using mine for now

    # delete curse word if match with the list
    if any(word in msg_content for word in marlyWord) and message.author.id == Marly and message.channel.id == gloomChannel:
        await message.channel.send('Bad Marly! Leave them to play GloomHaven')
        await message.delete(delay =3)
    elif not all(word in msg_content for word in marlyWord) and message.author.id == Marly and message.channel.id == gloomChannel:
        #Change Marlys comments to random upper lower case
        await message.channel.send(''.join([char.lower() if random.randint(0,1) else char.upper() \
                   for char in message.content]))
        await message.delete(delay =3)


client.run(os.getenv('TOKEN'))