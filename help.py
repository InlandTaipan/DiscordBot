#!/usr/local/bin/python3
import discord

#Help message that displays with -help command
async def sendHelp(message):
    #Embeded object containing help message
    helpMessage = discord.Embed(
        title="Yoshihiko Bot!",
        description = "Commands that are implemented:",
        url = "https://github.com/InlandTaipan/DiscordBot",
        colour = 14361758
    )

    helpMessage.set_footer(text = "If I'm being honest this bot is kinda poo")
    helpMessage.set_thumbnail(url =
        "https://interactive-examples.mdn.mozilla.net/media/examples/grapefruit-slice-332-332.jpg")
    helpMessage.set_author(name = "Maximo van der Raadt",
        icon_url = "https://cdn.discordapp.com/avatars/176130244095377411/1215eccfdd3410c40e8b80b7dff606b8.png?size=256")
        
    #Command List
    helpMessage.add_field(name = "-flipcoin", inline = False,
        value = "Flip a coin (heads or tails?)")
    helpMessage.add_field(name = "-roll [NUM]", inline = False,
        value = "Roll a dice (D4, D6, D8, D10, D12, D20)")
    helpMessage.add_field(name = "-help", inline = False,
        value = "Displays all commands (if you didn't know this one how did you get here?)")

    await message.channel.send(embed=helpMessage)
