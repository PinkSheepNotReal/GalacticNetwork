import discord
from discord.ext import commands
import traceback, os

# We use multiple files. This code help us to use the commands from those files. Info : The name of extensions are coming from : file name and folder name like at my first extension cogs.Commands
bot.load_extension("cogs.Commands")
bot.load_extension("cogs.docs")
bot.load_extension("cogs.Moderation")
bot.load_extension("cogs.Owner_commands")
bot.load_extension("cogs.error_handler")

# here we put the prefix for all commands
bot = commands.Bot(command_prefix='N.' , description='Galactic Network help Commands')
# This code removes the beggining help command
bot.remove_command('help')

# This event makes to put an : play game , status , and print something in cmd when bot is on
@bot.event
async def on_ready():
    await bot.change_presence(game=discord.Game(name='Galactic Netorks in! N.help'), status='dnd')
    print(bot.user.name)
    print(bot.user.id)

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
    embed1=discord.Embed(title="Fun Comands", color=0xff8080)
    embed1.add_field(name="cat", value= "See a random cat", inline=False)
    embed1.add_field(name="dog", value="See a random dog", inline=False)
    embed1.add_field(name="echo", value="make the bot to say something", inline=False)
    embed1.add_field(name="coinflip", value="Flip a coin", inline=False)
    embed1.add_field(name="hug", value="Hug someone", inline=False)
    embed1.add_field(name="pineapple", value="Take a pineapple :)", inline=False)
    embed2=discord.Embed(title="Help commands", color=0x0080ff)
    embed2.add_field(name="help", value="see this message", inline=False)
    embed2.add_field(name="support", value="join my support server", inline=True)
    embed2.add_field(name="ping", value= "check my ping!", inline=False)
    embed2.add_field(name="invite", value="invite me!", inline=True)
    embed2.add_field(name="avatar", value="Give avatar! Command in beta version", inline=False)
    embed3=discord.Embed(title="Docs commands", color=0xff8040)
    embed3.add_field(name="discord_py", value="Give a link to the Discord.py docs", inline=False)
    embed3.add_field(name="py_docs", value="Give a link to the python docs", inline=False)
    embed4=discord.Embed(title="OwnerCommands", color=0x000080)
    embed4.add_field(name="eval", value="evaluates a code", inline=False)
    embed4.add_field(name="repeat", value="reapeat a message some times", inline=False)
    embed4.add_field(name="poll", value="make a poll", inline=False)
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)
    await ctx.send(embed=embed3)
    await ctx.send(embed=embed4)

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
