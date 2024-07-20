import discord 
from dotenv import load_dotenv
import os
import re
from Game1 import NumberGuesserGame,UserInput_StoN
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
    
    if message.content.startswith('$Game1') and not Game1.Active:
        Game1.Turn = "User"
        Game1.Active = True
        await message.channel.send('Pick how high the number can go\n(Highest number is 100)')
    
    if Game1.Active:
        if Game1.Turn == "User":
            if message.content.startswith(f'${re.compile("[1-9]/d{1, 2}")}'):
                if Game1.HighNumber == "": 
                    Game1.HighNumber = UserInput_StoN(message)
                    await message.channel.send('Pick how low the number can go(Lowest number is 0)')
                elif Game1.LowNumber == "": 
                    Game1.LowNumber = UserInput_StoN(message)
                    await message.channel.send("Let's play")
                    await message.channel.send(f"Highest Number:{Game1.HighNumber} and Lowest Number:{Game1.LowNumber}")


client.run(os.getenv("TOKEN"))