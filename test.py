#!/usr/local/bin/python3

from dotenv import load_dotenv
load_dotenv()

import os
import asyncio
import discord

client = discord.Client()
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
    print("Ready for action!")

@client.event
async def on_message(message):
    if message.content == "Bob":
        await message.channel.send("BOOOOB")

client.run(TOKEN)
