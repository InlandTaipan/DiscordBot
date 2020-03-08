#!/usr/local/bin/python3
import random
import os
import diceArrays
import discord

CUR_PATH = os.path.dirname(__file__)

async def coinflip(message):
    result = random.randint(1,2)
    if result == 1:
        await message.channel.send("Heads!")
    elif result == 2:
        await message.channel.send("Tails!")
    else:
        await message.channel.send("Something went horribly wrong :/")

async def rollDice(message):
    try:
        numDice = int(message.content.split()[1])
    except:
        await message.channel.send(
            "Please tell me what kind of dice to roll, I'm not a mind reader!")
        return

    result = random.randint(1,numDice)

    if numDice == 20:
        if result == 20:
            await message.channel.send("NAT 20 baby, oh yeah!")
        elif result == 1:
            await message.channel.send("Thats a 1! Critical fail!")

    elif numDice == 6:
        newPath = os.path.relpath(diceArrays.D6[result - 1],CUR_PATH)
        await message.channel.send(file=discord.File(newPath))
