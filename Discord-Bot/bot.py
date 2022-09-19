# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print("Message posted to server, contents are: " + message.content)

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    spongebob_quote = "Is mayonaise an instrument?"
    response2 = ":)"

    if message.content == 'towel!':
        print("towel! detected in server message")
        response = random.choice(hitchhiker_quotes)
        print("repsonding with: " + response)
        await message.channel.send(response)

    if message.content == 'spongebob':
        print("spongebob detected in server message")
        response = spongebob_quote
        print("responding with: " + response)
        await message.channel.send(response)
        if message.content == 'yes':
            await message.channel.send(response2)
    if message.content == 'dogs'
        print("dogs detected in server message")
        print("responding with: image")
        await channel.send(file=discord.File('hercules.png'))
        await channel.send(file=discord.File('oreo.png'))


client.run(TOKEN)
