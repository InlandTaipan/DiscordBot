#!/usr/local/bin/python3
import random
import os
import diceArrays
import discord

CUR_PATH = os.path.dirname(__file__)

#Flips a coin and sends a message with the result
async def coinflip(message):
    result = random.randint(1,2)
    if result == 1:
        await message.channel.send("Heads!")
    elif result == 2:
        await message.channel.send("Tails!")
    else:
        await message.channel.send("Something went horribly wrong :/")

#Rolls a dice (size specified by user)
async def rollDice(message):
    #Makes sure dice type is specified
    try:
        numDice = int(message.content.split()[1])
    except:
        await message.channel.send(
            "Please tell me what kind of dice to roll, I'm not a mind reader!")
        return

    result = random.randint(1,numDice)

    #Find assets for D20
    if numDice == 20:
        if result == 20:
            await message.channel.send("NAT 20 baby, oh yeah!")
        elif result == 1:
            await message.channel.send("Thats a 1! Critical fail!")
        else:
            await message.channel.send(f"D20: {result}")

    #Find assets for D12
    elif numDice == 12:
        await message.channel.send(f"D12: {result}")
    
    #Find assets for D8
    elif numDice == 8:
        await message.channel.send(f"D8: {result}")
        
    #Find permanent assets for D6
    elif numDice == 6:
        diceImagePath = os.path.relpath(diceArrays.D6[result - 1],CUR_PATH)
        await message.channel.send(file=discord.File(diceImagePath))
    
    #Find permanent assets for D4
    elif numDice == 4:
        await message.channel.send(f"D4: {result}")
      
    #Debugging, might change later (idk if I want this to be a random number generator)
    else:
        await message.channel.send(f"D{numDice}: {result}")
