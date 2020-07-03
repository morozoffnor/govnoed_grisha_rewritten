import discord
from discord.ext import commands
import sys
sys.path.insert(1, '../functions')
from functions.cmd_print import cmd_print
from functions.embed import createSimpleEmbed
import asyncio

class Channel_settings(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def lock(self, ctx, cmd='help', arg='-a'):
        if cmd == 'help':
            embed = await createSimpleEmbed('Help', 'Чтобы ограничить количество слотов в канале, \n**находясь в нём**, напишите: ```!lock [количество_слотов]```')
            await ctx.send(embed=embed)
        else:
            try:
                await ctx.message.author.voice.channel.edit(user_limit=cmd)
                channel = ctx.message.author.voice.channel
                await cmd_print('debug', f'{ctx.author} locked channel {channel.name} for {cmd} slots!')
                embed = await createSimpleEmbed('Channel locked', f'Количество слотов в канале "{channel.name}" изменено! ')
                msg = await ctx.send(embed=embed)
                if arg == '-s':
                    await asyncio.sleep(1)
                    await msg.delete()
                    await cmd_print('debug', f'- [Lock] locking msg deleted (-s)')
                    await asyncio.sleep(1)
                    await ctx.message.delete()
                    await cmd_print('debug', f'- [Lock] user`s msg deleted (-s)')
                else:
                    await asyncio.sleep(10)
                    await ctx.message.delete()
                    await cmd_print('debug', f'- [Lock] locking msg deleted')
                    await asyncio.sleep(1)
                    await msg.delete()
                    await cmd_print('debug', f'- [Lock] user`s msg deleted')
            except:
                await cmd_print('error', f'{ctx.author} tried to lock channel for {cmd} slots and raised error')
                embed = await createSimpleEmbed('Unexpected error', 'Чтобы ограничить количество слотов в канале, \n**находясь в нём**, напишите: ```!lock [количество_слотов]```', color=0xd90000)
                await ctx.send(embed=embed)

    @commands.command()
    async def unlock(self, ctx):
        try:
            await ctx.message.author.voice.channel.edit(user_limit=0)
            channel = ctx.message.author.voice.channel
            await cmd_print('debug', f'{ctx.author} unlocked channel {channel.name}!')
            embed = await createSimpleEmbed('Channel unlocked', f'Ограничение на количество слотов в канале "{channel.name}" снято! ')
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(1)
            await msg.delete()
            await cmd_print('debug', f'- [unLock] unlocking msg deleted')
            await asyncio.sleep(1)
            await ctx.message.delete()
            await cmd_print('debug', f'- [unLock] user`s msg deleted')
        except:
            await cmd_print('error', f'{ctx.author} tried to unlock channel and raised error! Maybe they are not in the channel?')
            embed = await createSimpleEmbed('Unexpected error', 'Чтобы ограничить количество слотов в канале, \n**находясь в нём**, напишите: ```!lock [количество_слотов]```', color=0xd90000)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Channel_settings(client))
