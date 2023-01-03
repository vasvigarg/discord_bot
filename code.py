import discord
import os
from dotenv import load_dotenv
import requests

load_dotenv()

intents = discord.Intents().all()
client = discord.Bot(intents=intents)
token = os.getenv('TOKEN')
API_KEY = os.getenv('API_KEY')

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message {user_message} by {username} on {channel}')

    if message.author == client.user:
        return

    if channel == "general":
        if user_message.lower() == "hello" or user_message.lower() == "hi":
            await message.channel.send(f'Hello {username}! My name is Eorp, and I am programmed to keep you up to date on all the technology news that goes around the corner. \nType $news below for the same.')
            return
        elif user_message.lower() == "bye" or user_message.lower() == "bye eorp":
            await message.channel.send(f'Bye {username}. I hope I was able to help you in getting back on track.')

    if message.content == "$news":
        response = requests.get(f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}", params={"apiKey": API_KEY})
        data = response.json()
       
        output=""
        for article in data["articles"]:
            output += f"[{article['title']}]({article['url']})"
            output+="\n\n"
        embed=discord.Embed(title="News", description=f"**Latest News:** \n\n{output}", color=0x3584e4)
        await message.channel.send(embed=embed)
     
client.run(token)
