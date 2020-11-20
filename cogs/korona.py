import discord
from discord.ext import commands
import random
import sys
import json
sys.path.insert(1, '../functions')
from functions.cmd_print import cmd_print


class Korona(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def korona(self, ctx):
        cmd = ctx.message.content
        mention = cmd.lstrip("?korona ")
        
        with open("./data/korona.json") as json_data_file:
            data = json.load(json_data_file)

        if data["owner"] == mention:
            await ctx.send(f"{mention} уже и так владеет кароной. Ты вообще не можешь отобрать у человека карону, чтобы отдать её снова ему. Зачем? Ты нормальный вообще?")
        elif data["owner"] == ("<@!" + str(ctx.message.author.id) + ">"):
            print("<@!" + str(ctx.message.author.id) + ">")
            data["owner"] = mention
            file_object = open('./data/korona.json', 'w')
            json.dump(data, file_object)
            await ctx.send(f"{mention} теперь владеет кароной! Поздравляю, ты - долбоеб!")
        elif data["owner"] != ("<@!" + str(ctx.message.author.id) + ">"):
            print("<@!" + str(ctx.message.author.id) + "> is not equal to the data one")
            await ctx.send(f"пошел нахуй")
            
        

        




def setup(client):
    client.add_cog(Korona(client))