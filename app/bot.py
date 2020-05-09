import discord
from discord.ext import commands

TOKEN = 'your_token_id_here'

description = '''Bot Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello():
    """Says Hello World"""
    await bot.say("Hello World")

bot.run(TOKEN)