import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import os 
import random
import requests
import time

#response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")


class prices:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def price(self, *argv): #argv[0] is the crypto name(eg; BTC, ETH, LINK, etc.) and argv[1] is the currency code(eg: USD, EUR, etc.)
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]        
        response = requests.get("https://api.coinbase.com/v2/prices/"+ argv[0] + "-" + argv[1] +"/spot")
        data = response.json()
        currency = data["data"] ["base"]
        ogCurrency = data["data"] ["currency"]
        price = data["data"] ["amount"]
        embed = discord.Embed(name=currency, description='The price of ' + currency + " in " + ogCurrency, color=random.choice(colors))
        embed.add_field(name='Price', value=price, inline=False)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(prices(bot))