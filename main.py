import discord
from dotenv import load_dotenv
import os
from scrape import promos

load_dotenv()  # take environment variables from .env.

intents = discord.Intents.default()
intents.message_content = True
my_secret = os.getenv("TOKEN")

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('bbt'):
        for items in promos:
            await message.channel.send(items)


client.run(my_secret)