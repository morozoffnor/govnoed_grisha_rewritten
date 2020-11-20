import discord
from discord.ext import commands
import random
import sys
import json
sys.path.insert(1, '../functions')
from functions.cmd_print import cmd_print


class Who(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def who(self, ctx):
        with open("./data/korona.json") as json_data_file:
            data = json.load(json_data_file)
        await ctx.send(data["owner"])

        




def setup(client):
    client.add_cog(Who(client))