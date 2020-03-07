#!/usr/local/bin/python3

from dotenv import load_dotenv
load_dotenv()

import os
import discord
import coinsAndDice

client = discord.Client()
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print("Ready for action!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "-flipcoin".lower():
        await coinsAndDice.coinflip(message)

client.run(TOKEN)
