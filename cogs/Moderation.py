import discord
from discord.ext import commands
import asyncio
import time

class MODERATION():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user:discord.Member=None):
        if user == None:
            await ctx.send("Specify a user to ban it!")
        elif user == ctx.author.id:
            await ctx.send("You can't ban youserlf , dummy !")
        elif user.id == 414831660551634944:
        	await ctx.send("I will not ban myself!")
        else:
            await ctx.send("I banned {}".format(user.name))
            await user.ban()

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user:discord.Member=None):
        if user == None:
            await ctx.send("Specify a user to kick it!")
        elif user == ctx.author.id:
            await ctx.send("You can't kick youserlf , dummy !")
        elif user.id == 414831660551634944:
        	await ctx.send("I will not kick myself!")
        else:
            await ctx.send("I kicked {}".format(user.name))
            await user.kick()

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def mute(self, ctx, user:discord.Member=None):
        if user == None:
            await ctx.send("Specify a user to mute it!")
        elif user == ctx.author.id:
            await ctx.send("You can't mute youserlf , dummy !")
        elif user.id == 414831660551634944:
        	await ctx.send("I will not mute myself!")
        else:
            await ctx.send("I muted {}".format(user.name))
            await ctx.channel.set_permissions(user, send_messages=False)
            await asyncio.sleep(120)
            await ctx.channel.set_permissions(user, send_messages=True)
            await ctx.send("You are unmuted {} !".format(user.name))



def setup(bot):
    bot.add_cog(MODERATION(bot))
#Only for moderation
