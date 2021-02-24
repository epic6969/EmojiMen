import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from os import path
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

startSb()
