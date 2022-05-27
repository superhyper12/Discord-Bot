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
async def baowink(ctx):
    baowink = ["https://tenor.com/view/bao-ch-vtuber-whale-vtuber-wink-bao-gif-19044974"]
    await ctx.channel.send(random.choice(baowink))

@bot.command
async def baoblush(ctx):
	baoblush = ["https://tenor.com/view/bao-ch-whale-vtuber-blush-vtuber-bao-gif-19044975"]
	await ctx.channel.send(random.choice(baoblush))

@bot.command()
async def baodance(ctx):
	baodance = ["https://cdna.artstation.com/p/assets/images/images/038/802/010/original/tsu-drawing-animation-bao-halltaker-dance-pixel-minimalist-gif.gif?1624102562"]
	await ctx.channel.send(random.choice(baodance))

@bot.command()
async def baopocky(ctx):
	baopocky = ["https://cdn.donmai.us/sample/19/94/__bao_and_yuniiho_indie_virtual_youtuber_drawn_by_yuniiho__sample-1994c5c19a9fecde2c329640e60aa17a.jpg"]
	await ctx.channel.send(random.choice(baopocky))

@bot.command()
async def baokiss(ctx):
	baokiss = ["https://pbs.twimg.com/media/ElWCXoaW0AEWuhQ?format=jpg&name=large"]
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