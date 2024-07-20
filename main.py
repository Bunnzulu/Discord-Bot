import discord 
from dotenv import load_dotenv
import os
import re
from Game1 import NumberGuesserGame
load_dotenv(".env")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

Game1 = NumberGuesserGame()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$Hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$Game1'):
        Game1.Turn = "User"
        Game1.Active = True
        await message.channel.send('Pick how high the number can go')
    
    

client.run(os.getenv("TOKEN"))