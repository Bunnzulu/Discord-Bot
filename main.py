import discord 
from dotenv import load_dotenv
import os
import re
from Game1 import NumberGuesserGame,UserInput_StoN
from Game2 import Wordle
from Game3 import Quiz
load_dotenv(".env")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

Game1 = {}
Game2 = {}
Game3 = Quiz()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    user_id = message.author.id
    if message.author == client.user:
        return

    if message.content.startswith('$Hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('$Game1') and (user_id not in Game2 or not Game2[user_id].Active):
        if user_id not in Game1 or not Game1[user_id].Active:
            Game1[user_id] = NumberGuesserGame()
            Game1[user_id].Active = True
            Game1[user_id].Turn = "User"
            await message.channel.send(f'{message.author.mention}, Pick how high the number can go\n(Highest number is 999)')
        else:
            await message.channel.send(f'{message.author.mention}, you already have an active game.')
    
    if message.content.startswith('$Game2') and not Game2[user_id].Active:
        if user_id not in Game2 or not Game2[user_id].Active:
            Game2[user_id] = Wordle()
            Game2[user_id].Active = True
            await message.channel.send(f"{message.author.mention}, let's play")
            await message.channel.send("Hint: Start guessing 5-letter words, start with $")
            await message.channel.send("Type $ShowGuess to see how many attempts you have left.")
    
    if message.content.startswith('$Game3') and not Game3.Active:
        Game3.Active = True
        Game3.GetQuestion()
        await message.channel.send(f"Quiz is starting")
        await message.channel.send(f"{message.author.mention}\n {Game3.ShowQuestion()}")
        await message.channel.send("Type $(YourAnswerhere) to answer question")
    
    elif user_id in Game1 and Game1[user_id].Active:
        if Game1[user_id].Turn == "User":
            if message.content.startswith('$'):
                if not message.content.startswith('$0') and Game1[user_id].LowNumber == "":
                    if len(re.findall(r'\d{1,3}',message.content)):
                        if Game1[user_id].HighNumber == "": 
                            Game1[user_id].HighNumber = UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])
                            await message.channel.send(f'{message.author.mention}, Pick how low the number can go\n(Lowest number is 1)')
                        elif Game1[user_id].LowNumber == "": 
                            Game1[user_id].LowNumber = UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])
                            await message.channel.send(f"{message.author.mention}, Let's play")
                            Game1[user_id].Pick_random_Number()
                            await message.channel.send(f"{message.author.mention}, Highest Number: {Game1[user_id].HighNumber} and Lowest Number: {Game1[user_id].LowNumber}")
                            await message.channel.send(f"{message.author.mention}, Start guessing")
                elif not Game1[user_id].NumberGuessed and "" not in (Game1[user_id].HighNumber,Game1[user_id].LowNumber):
                    if len(re.findall(r'\d{1,3}',message.content)):
                        await message.channel.send(Game1[user_id].UserGuess(UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])))
                        await message.channel.send(f"{message.author.mention}, Guesses made:{Game1[user_id].UserGuesses}")
                        if Game1[user_id].NumberGuessed:
                            await message.channel.send(f"{message.author.mention},Now it's my turn")
                            await message.channel.send(f"{message.author.mention}, Pick your number")
                            Game1[user_id].Reset()
        elif Game1[user_id].Turn == "Bot":
            if message.content.startswith('$'):
                if Game1[user_id].AIHighNumber == 0 and not message.content.startswith('$0'):
                    if Game1[user_id].VerifyPickedNumber(UserInput_StoN(re.findall(r'\d{1,3}',message.content)[0])):
                        Game1[user_id].AIHighNumber = Game1[user_id].HighNumber
                        Game1[user_id].AILowNumber = Game1[user_id].LowNumber
                        await message.channel.send("I'm going to start guessing")
                        await message.channel.send(f"{message.author.mention}, Hint: type $BotGuess to continue")
                    else:
                        await message.channel.send(f"{message.author.mention}, Invalid Input")
                        await message.channel.send(f"{message.author.mention}, Highest Number:{Game1[user_id].HighNumber} and Lowest Number:{Game1[user_id].LowNumber}")
                elif message.content.startswith('$BotGuess'):
                    while not Game1[user_id].NumberGuessed:
                        await message.channel.send(Game1[user_id].AIGuess())
                    await message.channel.send(f"{message.author.mention}, You took {Game1[user_id].UserGuesses} guesses and I took {Game1[user_id].AIGuesses} guesses")
                    await message.channel.send(Game1[user_id].Winner())
                    await message.channel.send(f"{message.author.mention}, Game over!")
                    Game1[user_id].Reset(True)

    elif user_id in Game2 and Game2[user_id].Active:
        if message.content.startswith('$'):
            if message.content.startswith("$ShowGuess"):await message.channel.send(f"You have {Game2[user_id].Guesses} guesses left")
            if len(message.content) == 6 and not Game2[user_id].GuessCorrect and Game2[user_id].Guesses > 0:
                if Game2[user_id].Valid_Word(message.content[1:]):
                    await message.channel.send(Game2[user_id].Check_Guess(message.content[1:]))
                    if not Game2[user_id].GuessCorrect:
                        await message.channel.send(Game2[user_id].Display_Green())
                        await message.channel.send(Game2[user_id].Display_Yellow())
                        await message.channel.send(Game2[user_id].Display_Red())
                        Game2[user_id].WrongMessage = {"Green":[0,[],""],"Yellow":[0,[],""],"Red":[0,[],""]}
                    else:
                        await message.channel.send("Thanks for playing")
                        Game2[user_id].Active = False
                else:await message.channel.send("Invalid word")
            if Game2[user_id].Guesses == 0:
                await message.channel.send(f"The word was {Game2[user_id].Word}")
                await message.channel.send("Thanks for playing")
                Game2[user_id].Reset()
    
    elif Game3.Active:
        if message.content.startswith('$'):
            await message.channel.send(Game3.CheckAnswer(message.content[1:]))
            if Game3.Answered: 
                Game3.Answered = False
                if Game3.QNumber == 11: Game3.Complete = True
                else:
                    Game3.GetQuestion()
                    await message.channel.send(f"{message.author.mention}\n {Game3.ShowQuestion()}")
            if Game3.Complete:
                await message.channel.send(f"Quiz complete\n Score:{Game3.Score}/10")
                Game3.Reset()

client.run(os.getenv("TOKEN"))