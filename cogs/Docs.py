import discord
from discord.ext import commands

class Learning():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def discord_py(self, ctx):
        """Give a link to the Discord.py docs"""
        await ctx.send("**Here is a link to discord.py docs:**")
        await ctx.send("http://discordpy.readthedocs.io/en/rewrite/")
        await ctx.send("P.S from the site you can learn some good things")

    @commands.command()
    async def py_docs(self, ctx):
        """Give a link to the python docs""" 
        await ctx.send("**Resources for learning**")
        await ctx.send("https://automatetheboringstuff.com/ (for complete beginners to programming)")
        await ctx.send("https://learnxinyminutes.com/docs/python3/ (for people who know programming already)")
        await ctx.send("https://docs.python.org/3/tutorial/ (official tutorial)")
        await ctx.send("see also: http://www.codeabbey.com/ (exercises for beginners)")

def setup(bot):
    bot.add_cog(Learning(bot))

