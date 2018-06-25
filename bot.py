import discord
from discord.ext import commands
import traceback, os
import asyncio
import random

# We use multiple files. This code help us to use the commands from those files. Info : The name of extensions are coming from : file name and folder name like at my first extension cogs.Commands

# here we put the prefix for all commands
bot = commands.Bot(command_prefix='N.' , description='Galactic Network help Commands')
# This code removes the beggining help command
bot.remove_command('help')

bot.load_extension("cogs.Commands")
bot.load_extension("cogs.Docs")
bot.load_extension("cogs.Moderation")
bot.load_extension("cogs.Owner_commands")
bot.load_extension("cogs.error_handler")
bot.load_extension("cogs.eval")

# This event makes to put an : play game , status , and print something in cmd when bot is on
@bot.event
async def on_ready():
    presence = [
        "N.help | Loading Networks...",
        "N.help | Playing with pepole",
        "N.help | Helping pepole",
        "N.help | Seeing my friends",
        "N.help | Thinking for new commands",
        f"N.help | Playing with {len(bot.guilds)} servers!"
    ]
# the list can be as long as you want, just add more.
    while True:
        await bot.change_presence(activity=discord.Game(name=random.choice(presence)))
        await asyncio.sleep(20)
        
        
def has_role_in_my_server(name):
    def wrapper(ctx):
        x = discord.utils.get(bot.guilds, id=416562446506000386)
        role = discord.utils.get(x.roles, name=name)
        if role in ctx.author.roles:
            return True
        return False
    return commands.check(wrapper)

#@bot.event
# def on_member_join(member):
    #await ctx.send(member, member.name + " Welcome to **" + member.server.name + "**!")


# Here we maked our help command
@bot.command()
async def help(ctx):
    embed1=discord.Embed(title="My commands", color=0xff8080)
    embed1.add_field(name="Fun", value= "`cat`, `dog`, `echo`, `flip`, `hug`, `pineapple`", inline=False)
    embed1.add_field(name="Help", value="`help`, `support`, `ping`, `invite`, `avatar(wip)`", inline=False)
    embed1.add_field(name="Docs", value="`discord_py`, `py_docs`", inline=False)
    embed1.add_field(name="OwnerCommands", value="`eval`, `repeat`, `poll`", inline=False)
    embed1.add_field(name="ModerationCommands", value="`ban`, `kick`, `mute`", inline=False)
    await ctx.send(embed=embed1)

@bot.command()
@has_role_in_my_server("Bot Ultra Helper")
async def hello(ctx):
    await ctx.send("Hello Ultra Helper!")
    


# Here we make a little error handler for extensions

#if __name__ == '__main__':
    #for extension in startup_extensions:
        #try:
            #bot.load_extension(extension)
        #except Exception as e:
            #print('Failed to load {ex}'.format(ex=extension))
            #traceback.print_exc()

# Here we put our bot token to make the all code work

if not os.environ.get('TOKEN'):
    print("no token found")
bot.run(os.environ.get('TOKEN').strip('"'))
