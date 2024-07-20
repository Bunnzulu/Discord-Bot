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
        await message.channel.send('Pick how high the number can go\n(Highest number is 999)')
    
    elif Game1.Active:
        if Game1.Turn == "User":
            if message.content.startswith('$'):
                if not message.content.startswith('$0') and Game1.LowNumber == "":
                    if len(re.findall(r'\d{1,3}',message.content)):
                        if Game1.HighNumber == "": 
                            Game1.HighNumber = UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])
                            await message.channel.send('Pick how low the number can go\n(Lowest number is 1)')
                        elif Game1.LowNumber == "": 
                            Game1.LowNumber = UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])
                            await message.channel.send("Let's play")
                            Game1.Pick_random_Number()
                            await message.channel.send(f"Highest Number:{Game1.HighNumber} and Lowest Number:{Game1.LowNumber}")
                            await message.channel.send("Start guessing")
                elif not Game1.NumberGuessed:
                    if len(re.findall(r'\d{1,3}',message.content)):
                        await message.channel.send(Game1.UserGuess(UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])))
                        await message.channel.send(f"Guesses made:{Game1.UserGuesses}")
                        if Game1.NumberGuessed:
                            await message.channel.send("Now it's my turn")
                            Game1.Reset()



client.run(os.getenv("TOKEN"))