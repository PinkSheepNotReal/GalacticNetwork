import discord
from discord.ext import commands
import textwrap
import traceback
from contextlib import redirect_stdout
import random
import datetime
import aiohttp


class MemberCommands():
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
        """Pong!"""
        em = discord.Embed(title="Pong!", description="Your ping: {} ms".format(round(self.bot.latency*1000, 1)), colour=discord.Colour.orange())
        await ctx.send(embed=em)
    
    @commands.command(aliases=['about'])
    async def info(self, ctx):
        """some info about the bot"""
        info = discord.Embed(title="Info", color=discord.Colour.blue())
        info.add_field(name="**Bot Owner:**", value="[Galactic] Capitan Rex The Clone#9168", inline=False)
        info.add_field(name="**Credits at commands/codes:**", value="Twelve, Cool, Kingalma, Haunt, [60hz] Saggytarius, Maninder, Moog, JellyWX, Gerasimenko, Vilgot, Dot, kxnzy  ", inline=False)
        await ctx.send(embed=info)

    @commands.command(aliases=["invitation"])
    async def invite(self, ctx):
        """invite me"""
        await ctx.send("<:down_arrow:421275124688355330> BOT invite <:down_arrow:421275124688355330>")
        await ctx.send('https://discordapp.com/oauth2/authorize?client_id=414831660551634944&scope=bot&permissions=35840')
    
    @commands.command(aliases=["PyHelp"])
    async def PythonHelp(self, ctx):
        """The server how helped me go in ;)"""
        channel = ctx.message.author
        embed = discord.Embed(title="Join this server for Python help", url="https://discord.gg/SAj6U6m", color=discord.Colour.red())
        await channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def cat(self, ctx):
        """Shows a random cat"""
        api = "http://aws.random.cat/meow"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as r:
                if r.status == 200:
                    response = await r.json()
                    embed = discord.Embed(color = 0xff0000)
                    embed.set_author(name = "{} here is your random cat".format(ctx.message.author.name))
                    embed.set_image(url = response["file"])
                    await ctx.send(embed = embed)

    @commands.command(aliases=["flip"])
    async def coinflip(self, ctx):
        choice = random.randint(1,2)
        if choice == 1:
            embed=discord.Embed(title="you flipped tails", color=0xff0000)
            embed.set_image(url="https://image.prntscr.com/image/XIhcumqjRB_FjHzPCz-jOQ.png")
            await ctx.send(embed=embed)
        if choice == 2:
            embed=discord.Embed(title="You flipped heads", color=0xff0000)
            embed.set_image(url="https://image.prntscr.com/image/rco6mQybS7aJcqfW7RK59Q.png")
            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, *, member : discord.Member=None):
        """Hug someone"""
        if member is None:
            await ctx.send("{} has been hugged! 💘".format(ctx.message.author.mention))
        elif member.id == ctx.message.author.id:
            await ctx.send("{} hugged themselves because they are a loner 🤦".format(ctx.message.author.mention))
        else:
            await ctx.send("{} was hugged by {} 💝".format(member.mention, ctx.message.author.mention))
    
    @commands.command(pass_context=True)
    async def echo(self, ctx, *, echo: str):
        '''Speaks for you'''
        if echo.__contains__("@everyone") or echo.__contains__("@here"):
            try:
                await ctx.message.delete()
            except: pass
            await ctx.send(f"{ctx.author.mention}, Really ? You think you're smart enough to fool me ? :smirk:")
            return
        else:
            try:
                await ctx.message.delete()
            except:
                pass
            await ctx.send(echo)


    @commands.command()
    async def support(self, ctx):
        """A invite to the bot server"""
        channel = ctx.message.author
        embed = discord.Embed(title="Join this server for support", url="https://discord.gg/wSKR2JM", color=discord.Colour.blue())
        await channel.send(embed=embed)

    @commands.command(pass_context=True)
    async def dog(self, ctx):
        """Shows a random dog"""
        api = "https://api.thedogapi.co.uk/v2/dog.php"
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as r:
                if r.status == 200:
                    response = await r.json()
                    embed = discord.Embed(color = 0x00ff44)
                    embed.set_author(name = "{} here is your random dog".format(ctx.message.author.name))
                    embed.set_image(url = response['data'][0]["url"])
                    await ctx.send(embed = embed)

    @commands.command()
    async def pineapple(self, ctx):
        """Free pineapple"""
        await ctx.send(":pineapple: do you want him? <:cutedPineapple:421196499230261248> i cuted him for you! :yum:")

    @commands.command()
    async def test(self, ctx):
        if ctx.author.id == 393807627995578370:
            await ctx.send("im here :slight_smile: ")
        else:
            await ctx.send("This is working! You dont see?")

    @commands.command()
    async def none(self, ctx):
        await ctx.send(("""```css

            hello

            hi

            hey

            ```"""))

    @commands.command()
    async def reaction(self, ctx):
        x = await ctx.send("reaction")
        await x.add_reaction("<:tada:427429630283218945>")

    @commands.command()
    async def userinfo(self, ctx):
        embed = discord.Embed(title="User Info", colour=0xff8080)
        embed.add_field(name="ID", value="{}".format(ctx.author.id), inline=False)
        embed.add_field(name="UserName", value="{}".format(ctx.author.name), inline=False)
        embed.add_field(name="Status", value="{}".format(ctx.author.status), inline=False)
        await ctx.send(embed=embed)
            
    @commands.command()
    async def avatar(self, ctx):
        avatar = discord.Embed(title="{}'s avatar".format(ctx.author.name), color=discord.Colour.orange())
        avatar.add_field(name="{}".format(User.avatar_url), inline=False)
        await ctx.send(embed=avatar)
        
    @commmands.command(pass_context=True)
    async def AskBall(ctx):
        choice = random.randint(1,3)
        if choice == 1:
                await ctx.send("Yes")
        if choice == 2:
                await ctx.send("No")
        if choice == 3:
    	        await ctx.send("Maybe")

 

def setup(bot):
    bot.add_cog(MemberCommands(bot))
