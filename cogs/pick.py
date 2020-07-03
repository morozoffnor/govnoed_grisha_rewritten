import discord
from discord.ext import commands
import random
import sys
sys.path.insert(1, '../functions')
from functions.cmd_print import cmd_print


class Pick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pick(self, ctx):
        cmd = ctx.message.content
        string = cmd.lstrip("!pick ")
        options = string.split(", ")
        l = len(options)
        answer = random.randrange(0, l, 1)
        await ctx.send(options[answer])

        # await cmd_print('debug', f'{options}')




def setup(client):
    client.add_cog(Pick(client))
