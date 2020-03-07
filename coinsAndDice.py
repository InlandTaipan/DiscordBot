#!/usr/local/bin/python3
import random

async def coinflip(message):
    result = random.randint(1,2)
    if result == 1:
        await message.channel.send("Heads!")
    elif result == 2:
        await message.channel.send("Tails!")
    else:
        await message.channel.send("Something went horribly wrong :/")

async def rollDice(message):
    message.content
