#!/usr/local/bin/python3

#Loading bot token (its a secret, shhhh!)
from dotenv import load_dotenv
load_dotenv()

import os
import discord

#My modules
import coinsAndDice #Functions for flipping a coin and rolling dice
import help #Display help message

#Setting up client
client = discord.Client()
TOKEN = os.getenv("TOKEN")

#Message when bot is ready for commands
@client.event
async def on_ready():
    print("Ready for action!")
    await client.change_presence(activity = discord.Activity(
        name = "fruit expire",
        type = discord.ActivityType.watching)
    )

#Bot command list
@client.event
async def on_message(message):
    #Prevent bot from responding to its own messages
    if message.author == client.user:
        return

    #flipcoin command
    if message.content.lower() == "-flipcoin":
        await coinsAndDice.coinflip(message)
    #dice roll command
    elif message.content.lower().startswith("-roll"):
        await coinsAndDice.rollDice(message)
    #help command
    if message.content.lower() == "-help":
        await help.sendHelp(message)

client.run(TOKEN)
