import discord
from discord.ext import commands
import random
import sys
sys.path.insert(1, '../functions')
from functions.cmd_print import cmd_print


class Roll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def roll(self, ctx, *, number=100):
        generatedNumber = random.randrange(1, number, 1)
        await ctx.send(generatedNumber)
        await cmd_print('debug', f'Generated number - {generatedNumber}')


def setup(client):
    client.add_cog(Roll(client))
