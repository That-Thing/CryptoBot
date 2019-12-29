import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import json
import os 
import random
import requests
import time
import urllib.request

#response = requests.get("https://api.coinbase.com/v2/prices/BTC-USD/spot")


class prices:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def price(self, *argv): #argv[0] is the crypto name(eg; BTC, ETH, LINK, etc.) and argv[1] is the currency code(eg: USD, EUR, etc.)
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]      
        cryptoID = argv[0] + "-" + argv[1]  
        response = requests.get("https://api.coinbase.com/v2/prices/"+ cryptoID +"/spot")
        data = response.json()
        currency = data["data"] ["base"]
        ogCurrency = data["data"] ["currency"]
        price = data["data"] ["amount"]
        embed = discord.Embed(name=currency, description='The price of ' + currency + " in " + ogCurrency, color=random.choice(colors))
        embed.add_field(name='Price', value=price, inline=False)
        await self.bot.say(embed=embed)


    #get 24 hours stats for whatever crypto the user indicates
    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def stats(self, *argv):
        cryptoID = argv[0] + "-" + argv[1]
        colors = [0xff0000, 0xff8100, 0xfdff00, 0x15ff00, 0x15ff00, 0x0045ff, 0x9600ff, 0xff00b4]        
        response = requests.get("https://api.pro.coinbase.com/products/"+ cryptoID +"/stats")
        data = response.json()
        high = data["high"]
        low = data["low"]
        volume = data["volume"]
        current = data['last']
        embed = discord.Embed(name=argv[0], description="24 Hours stats for " + argv[0], color=random.choice(colors))
        embed.add_field(name='Current', value=current, inline=True)
        embed.add_field(name='High', value=high, inline=True)
        embed.add_field(name='Low', value=low, inline=True)
        embed.add_field(name='Amount Transferred', value=volume, inline=True)
        await self.bot.say(embed=embed)



#RTS: MAke the fucking graph command. 

    @commands.command()
    @commands.cooldown(rate=1, per=2.0)
    async def graph(self, *argv):
        cryptoID = argv[0] + "-" + argv[1]
        startDate = argv[2]
        response = requests.get("https://api.pro.coinbase.com/products/" + cryptoID + "/candles?start=" + startDate + "GMT12:00:00" +"&granularity=900")
        data = response.json()
        i=0
        for x in data:
            #print(data[1])
            i=i+1
            print(i)


def setup(bot):
    bot.add_cog(prices(bot))