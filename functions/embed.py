import discord

async def createSimpleEmbed(title, description, *, timestamp=0, footer='0', color=0):
    embed = discord.Embed(title=title, description=description, color=color)
    if timestamp != 0:
        embed.timestamp()
    if footer != '0':
        embed.set_footer(text=footer)

    return embed