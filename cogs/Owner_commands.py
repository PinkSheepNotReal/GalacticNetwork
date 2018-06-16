import discord
from discord.ext import commands
import datetime


class OwnerCommands():
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def poll(self, ctx, *, message):
        """Make a poll"""
        author = ctx.message.author
        embed = discord.Embed(color=author.color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name="Poll", icon_url=author.avatar_url)
        embed.description = message
        embed.set_footer(text=author.name)
        x = await ctx.send(embed=embed)
        await x.add_reaction("👍")
        await x.add_reaction("\U0001f937")
        await x.add_reaction("👎")

    @commands.is_owner()
    @commands.command(pass_context=True)
    async def repeat(self, ctx, times: int,*, content : str):
        for i in range(times):
            await ctx.send(content)

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, code):
        await ctx.send(eval(code))

    @commands.is_owner()
    @commands.command()
    async def sudo(self, ctx, member: discord.Member, *, command):
        """Invoke a command as if you were another user."""
        ctx.message.author = member
        ctx.message.content = f"{ctx.prefix}{command}"
        await ctx.bot.process_commands(ctx.message)    


def setup(bot):
    bot.add_cog(OwnerCommands(bot))

# Those are owner commands. Only the bot owner can use them
