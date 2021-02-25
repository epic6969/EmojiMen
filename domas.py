import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from os import path
import os
from time import sleep
import requests

TOKEN = ""
PREFIX = ";"

client = discord.Client()
sb = Bot(command_prefix=PREFIX, self_bot=True)
sb.remove_command("help")

def startSb():
    global TOKEN
    TOKEN = ""
    try:
        TOKEN = open("Token.txt", "r").read()
        if TOKEN == "":
            raise Exception("Token cannot be empty")
    except:
        TOKEN = input("Token: ")
        open("Token.txt", "w").write(TOKEN)
    sb.run(TOKEN, bot=False)

@sb.event
async def on_ready():
    print("Let's go bro!!")

# Emoji - Sends any emoji as link/attachment.
@sb.command()
async def emoji(ctx):
    await print("hello bro")

# Search - Search for emoji in your files.
@sb.command()
async def search(ctx):
    await print("hello bro")

# Dump - Dumps all emojis in a guild.
@sb.command()
async def dump(ctx):
    await print("hello bro")

# Clear - Clears console screen.
@sb.command()
async def clear(ctx):
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")

# Help - SHows a list of all commands.
@sb.command()
async def help(ctx):
    await print("Here's a list of all the commands:\n*Help - Shows a list of all commands.\n*Dump - Dumps all emojis in a guild\n*Search - Search for an emoji.\n*Emoji - Use an emoji from your files.\n*Clear - Clears console screen.")

clear()
startSb()
