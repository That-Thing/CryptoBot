import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random

class help:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True, aliases=['Help'])
    @commands.cooldown(rate=1, per=2.0)
    async def help(self, ctx):
        author = ctx.message.author
        
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]
        embed = discord.Embed(title="Commands", colour=random.choice(colors))
        embed.add_field(name='c!price *crypto code* *currency code*', value='Gets the current price for the cryptocurrency', inline=True)
        await self.bot.send_message(author, embed=embed)
        await self.bot.say('{}, take a look in your DMs'.format(author.mention))
        




def setup(bot):
    bot.add_cog(help(bot))