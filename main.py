from logging import PlaceHolder
from re import A, search
from typing import Optional
from asyncio.tasks import wait_for
from discord import activity, message, role
from discord.channel import VoiceChannel
from discord.ext.commands import bot, context
from discord.ext.commands.converter import RoleConverter
from discord.ext.commands.core import check, command
import discord
import os
from discord.ext import commands
from discord_components import DiscordComponents, Select, SelectOption
from discord.ext import commands
from discord.utils import get
from discord_components import *
import datetime
from datetime import datetime
from dotenv import load_dotenv
import random
load_dotenv()
TOKEN = os.getenv('TOKEN')


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())



@bot.event
async def on_ready():
	await client.change_presence(activity=discord.Streaming(name="DisguisedToast", url="https://www.twitch.tv/disguisedtoast"))
	print("Chirithy is now online")

#Music commad--------------------------------------------------------------------------------------------------------------------------------------------------

@bot.command(name='ping', help="This command return the latency")
async def ping(ctx):
	await ctx.send(f'**Ping** Latency: {round(client.latency * 1000)}ms')


@bot.command(pass_context = True)
async def join(ctx):
	if (ctx.author.voice):
		channel = ctx.message.author.voice.channel
		await channel.connect()
	else:
		await ctx.send("You are not in a voice channel.")


@bot.command(pass_context = True)
async def leave(ctx):
	if (ctx.voice_client):
		await ctx.guild.voice_client.disconnect()
		await ctx.send("Bao has left the voice channel")
	else:
		await ctx.send("I am not in a voice channel")

@bot.command()
async def play(ctx, * url):
	player = music.get_player (guild_id=ctx.guild.id)
	if not player:
		player = music.create_player(ctx, ffmpeg_error_betterfix=True)
	if not ctx.voice_client.is_playing():
		await player.queue(url, search=True)
		song = await player.play()
		await ctx.send(f"I have started playing  '{song.name}' ")
	else:
		song = await player.queue(url, search=True)
		await ctx.send(f'{song.name} has been aded to playlist')

#Bot_Interaction-----------------------------------------------------------------------------------------------------------------------------------------------

@bot.command()
async def bugcatweary(ctx):
    baowink = ["https://giphy.com/gifs/cat-capoo-bugcat-3o7bufrhglm1BTsfra"]
    await ctx.channel.send(random.choice(baowink))

@bot.command
async def bugcatflip(ctx):
	baoblush = ["https://giphy.com/gifs/meme-capoo-bugcat-JsVlBMEaHdOEGQKLXB"]
	await ctx.channel.send(random.choice(baoblush))

@bot.command()
async def bugcatwiggle(ctx):
	baodance = ["https://giphy.com/gifs/capoo-cat-3ov9jZ0V6gOO0oa98Y"]
	await ctx.channel.send(random.choice(baodance))

@bot.command()
async def bugcatshy(ctx):
	baopocky = ["https://giphy.com/gifs/capoo-3o7aCYnXnYF5T5sxlm"]
	await ctx.channel.send(random.choice(baopocky))

@bot.command()
async def bugcatboo(ctx):
	baokiss = ["https://giphy.com/gifs/capoo-halloween-3ov9k0OmfNYeLdK4gg"]
	await ctx.channel.send(random.choice(baokiss))



# #Guild command-----------------------------------------------------------------------------------------------------------------------------------------------
@bot.command()
async def getlist(ctx):
	guild = client.get_guild(923679032938209351)
	print("Server found!")
	for member in guild.members:
		print(member)



#Checktime----------------------------------------------------------------------------------------------------------------------------------------------------






#EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE
client.run(TOKEN)
