import discord
from discord.ext import commands

import json
import os
import asyncio
import requests


with open('config.json') as json_data_file:
    config = json.load(json_data_file)

client = commands.Bot(command_prefix=[config['bot_prefix']])


@client.event
async def on_message(ctx):
    author = ctx.author
    content = ctx.content
    print(f'{author}: {content}')
    await client.process_commands(ctx)


@client.event
async def on_ready():
    print(
        f'Ready! Using {client.user.name}#{client.user.discriminator}`s bot account')
    activeGuilds = client.guilds
    count = 0
    for s in activeGuilds:
        count += len(s.members)
    print(f"Servers connected: {len(client.guilds)}, Users: {count}")


@client.command(hidden=True)
async def load(ctx, *, extension):
    client.load_extension(f'cogs.{extension}')
    print(f'Extension "{extension}" loaded')
    msg = ctx.message
    message = await ctx.send('Модуль загружен')
    await asyncio.sleep(4)
    await message.delete()
    await msg.delete()


@client.command(hidden=True)
async def unload(ctx, *, extension):
    client.unload_extension(f'cogs.{extension}')
    print(f'Extension "{extension}" unloaded')
    msg = ctx.message
    message = await ctx.send('Модуль выгружен')
    await asyncio.sleep(4)
    await message.delete()
    await msg.delete()


@client.command(hidden=True)
async def reload(ctx, *, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'Extension "{extension}" reloaded')
    msg = ctx.message
    message = await ctx.send('Модуль перезагружен')
    await asyncio.sleep(4)
    await message.delete()
    await msg.delete()


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(config["token"])
