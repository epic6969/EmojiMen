import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from os import path
import os
import requests
from config import TOKEN, PREFIX

client = discord.Client()
sb = Bot(command_prefix=PREFIX, self_bot=True)
sb.remove_command("help")

@sb.event
async def on_ready():
    print("Ready!")

# Emoji - Sends any emoji as link or attachment.
@sb.command()
async def emoji(ctx, emojiName):
    await ctx.message.delete()
    emoji = getEmojiFromName(emojiName)
    try:
        await ctx.send(file=discord.File(emoji))
    except:
        if emoji != "EmojiNotFound":
            await ctx.send(content=emoji.url)
    print("[ERROR]: Couldn't find any emojis matching your search!" if emoji == "EmojiNotFound" else "[SUCCESS]: Found and sent emoji: "+str(emoji))
    
def getEmojiFromName(name):
    currentDir = os.getcwd()
    for r, d, f in os.walk(currentDir):
        for file in f:
            if file.endswith(".png") or file.endswith(".gif"):
                if name in file:
                    return os.path.join(r, file)
    for guild in sb.guilds:
            for emoji in guild.emojis:
                if name in emoji.name:
                    return emoji
    return "EmojiNotFound"

# Search - Search for emoji.
@sb.command()
async def search(ctx, searchQuery):
    await ctx.message.delete()
    result = getEmojiFromName(searchQuery)
    print("[ERROR]: Couldn't find any emojis matching your search!" if result == "EmojiNotFound" else "[SUCCESS]: Found emoji: "+str(result))

# Dump - Dumps all emojis in a guild.
@sb.command()
async def dump(ctx):
    await ctx.message.delete()
    for emoji in ctx.message.guild.emojis:
        r = requests.get(emoji.url)
        path = ctx.message.guild.name+"/".strip()
        if os.path.exists(path) == False:
            os.mkdir(path)
        with open(path+emoji.name+".gif" if emoji.animated else path+emoji.name+".png", "wb") as f:
            f.write(r.content)
    print("[DONE]: Downloaded all emojis from"+ctx.message.guild.name+"!")

# Clear - Clears console screen.
@sb.command()
async def clear(ctx):
    await ctx.message.delete()
    _ = os.system("clear") if os.name == "posix" else os.system("cls")
    print("[DONE]: Cleared Console!")

# Help - Shows a list of all commands.
@sb.command()
async def help(ctx):
    await ctx.message.delete()
    print("Here's a list of all the commands:\n*Help - Shows a list of all commands.\n*Dump - Dumps all emojis in a guild\n*Search - Search for an emoji.\n*Emoji - Use an emoji from your files.\n*Clear - Clears console screen.")

if os.path.exists("Emojis") != True:
    os.mkdir("Emojis")
sb.run(TOKEN, bot=False)
