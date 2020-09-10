import os
import random
import discord
from discord.ext import commands




def obscure(message):
    i = 0
    st = ""
    while i < len(message):
        if i == random.randint((0+i-6),i) :
            st = st + " krrshh "
            i = i + 1
        else:
            st = st+message[i]
        i = i + 1
    
    return st

def cricri(message):
    st = "Bzt "
    st = st + message + " Bzt"
    return st
            
client = discord.Client()

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="Se casse les dents", url="http://www.twitch.tv/zamanite"))
    print('My Ready is Body')
@client.event
async def on_message(message):
    if str(message.channel) == "channel-where-message-is-sent-and-deleted" and message.content != "":
        channel = client.get_channel(CHANNEL_ID)
        channeladmin = client.get_channel(CHANNEL_ADMIN_ID)
        radiomsg = obscure(message.content)
        radiomsg2 = cricri(radiomsg)
        await channel.send(radiomsg2)
        await channeladmin.send(message.author)
        await message.channel.purge(limit=1)
    if str(message.channel) == "channel-where-the-message-is-sent" and str(message.author.id) == "BOT-ID":
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(message.id)

client.run('BOT-TOKEN')
