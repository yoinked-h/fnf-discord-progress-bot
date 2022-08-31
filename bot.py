
import ast
import discord
from discord.ext import commands
import random

description = '''fnf progress tracker'''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='?', description=description, intents=intents, help_command=None)


@bot.event
async def on_ready():
    global f
    #aaaargh, globals are always a mixed bag
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')
    try:
        f = open("data.txt", "r").read()
        f = ast.literal_eval(f)
    except:
        #the file is not there, or ast dun goofed
        f = {
            123:  [0,0,0,0,0,0],
            456: [0,0,0,0,0,0] #replace 123 and 456 with channel id's
        }
        open("data.txt", "w").write(str(f))


@bot.command()
async def help(ctx):
    """Help command."""
    await ctx.send("""Hello, this bot has like 7 commands:
    `?coding [progress]`
    `?art [progress]`
    `?song [progress]`
    `?background [progress]`
    `?chart [progress]`
    `?animation [progress]`
    `?getprogress`
    The bot will detect the channel and update the stored data.
    So for example, `?coding 100` will mean that the coding is done, and so on.
    """)
#The order should be like so, coding, art, song, background, chart and finally anim
def pretty(inList):
    final = """"""
    print("check zero")
    i = 0
    order = ["Coding", "Art", "Song", "Background", "Chart", "Animation", "filler"]
    while i != 6:
        final = final + order[i] + " progress: " + str(inList[i]) + "%\n"
        i += 1
    print("check one")
    try:
        final = final + f"Total progress: {sum(inList) / len(inList)}%"
    except:
        final = final + f"Total progress: 0%"
    print("check two")
    return final
@bot.command()
async def coding(ctx, how: int):
    """Update the code progress."""
    try:
        if how > 100:
            how = 100
        elif how < 0:
            how  = 0
        f[ctx.message.channel.id][0] = how
        await ctx.send("Updated!, total progress: \n" + pretty(f[ctx.message.channel.id]))
    except Exception as e:
        await ctx.send("uhoh, blame yoinked for coding this in 30 min, heres the error (it has not updated the thing): \n" + str(e))

@bot.command()
async def art(ctx, how: int):
    """Update the art progress."""
    try:
        if how > 100:
            how = 100
        elif how < 0:
            how  = 0
        f[ctx.message.channel.id][1] = how
        await ctx.send("Updated!, total progress: \n" + pretty(f[ctx.message.channel.id]))
    except Exception as e:
        await ctx.send("uhoh, blame yoinked for coding this in 30 min, heres the error (it has not updated the thing): \n" + str(e))

@bot.command()
async def song(ctx, how: int):
    """Update the song progress."""
    try:
        if how > 100:
            how = 100
        elif how < 0:
            how  = 0
        f[ctx.message.channel.id][2] = how
        await ctx.send("Updated!, total progress: \n" + pretty(f[ctx.message.channel.id]))
    except Exception as e:
        await ctx.send("uhoh, blame yoinked for coding this in 30 min, heres the error (it has not updated the thing): \n" + str(e))

@bot.command()
async def background(ctx, how: int):
    """Update the bg progress."""
    try:
        if how > 100:
            how = 100
        elif how < 0:
            how  = 0
        f[ctx.message.channel.id][3] = how
        await ctx.send("Updated!, total progress: \n" + pretty(f[ctx.message.channel.id]))
    except Exception as e:
        await ctx.send("uhoh, blame yoinked for coding this in 30 min, heres the error (it has not updated the thing): \n" + str(e))

@bot.command()
async def chart(ctx, how: int):
    """Update the chart progress."""
    try:
        if how > 100:
            how = 100
        elif how < 0:
            how  = 0
        f[ctx.message.channel.id][4] = how
        await ctx.send("Updated!, total progress: \n" + pretty(f[ctx.message.channel.id]))
    except Exception as e:
        await ctx.send("uhoh, blame yoinked for coding this in 30 min, heres the error (it has not updated the thing): \n" + str(e))

@bot.command()
async def animation(ctx, how: int):
    """Update the anim progress."""
    try:
        if how > 100:
            how = 100
        elif how < 0:
            how  = 0
        f[ctx.message.channel.id][5] = how
        await ctx.send("Updated!, total progress: \n" + pretty(f[ctx.message.channel.id]))
    except Exception as e:
        await ctx.send("uhoh, blame yoinked for coding this in 30 min, heres the error (it has not updated the thing): \n" + str(e))

@bot.command()
async def getprogress(ctx):
    """Get the progress."""
    try:
        await ctx.send("Total progress: \n" + pretty(f[ctx.message.channel.id]))
    except Exception as e:
        await ctx.send("uhoh, blame yoinked for coding this in 30 min, heres the error (it has not updated the thing): \n" + str(e))


bot.run('token')
