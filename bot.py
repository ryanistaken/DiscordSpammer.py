import discord
from discord.ext import commands, tasks
import os
from discord.ext.commands.core import command
from dotenv import load_dotenv
import asyncio

load_dotenv()

BOT_PREFIX = os.getenv("PREFIX")
BOT_TOKEN = os.getenv("TOKEN")
BOT_MESSAGE = os.getenv("MESSAGE")

bot = commands.Bot(command_prefix=BOT_PREFIX)

bot.remove_command('help')

@tasks.loop(seconds=1)
async def spam(ctx):
    await ctx.send(BOT_MESSAGE)

@bot.command()
async def run(ctx):
    spam.start(ctx)

bot.run(BOT_TOKEN)