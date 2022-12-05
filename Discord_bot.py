
import discord
from discord.ext 
import commands
import praw 
import random

client = commands.Bot(command_prefix = '!')

bad_words = ["abe","saale","kutte"]


@client.command()
async def hello(ctx):
    if str(ctx.author) == "": //Discord_username
        await ctx.send(f"Hello {ctx.author}")

@client.command()
async def yoda(ctx):
    await ctx.send(file=discord.File("baby.jpg"))

@client.command()
async def youtube(url):
    await url.send("https://youtu.be/ccSvNoLcnfs")


@client.command()
async def madad(ctx):
    embed = discord.Embed(title="Commands",description="Some useful commands")
    embed.add_field(name="!hello",value="Bot send's you Hello",inline=True)
    embed.add_field(name="!yoda",value="yoda pic",inline=False)

    await ctx.send(content=None,embed=embed)

@client.event
async def on_message(message):
    message.content = message.content.lower()
    for word in bad_words:
        if message.content.count(word)  greater sign 0:
            await message.channel.purge(limit=1)

    await client.process_commands(message)



reddit = praw.Reddit(client_id='your clientid',
                     client_secret='Your client secret',
                     user_agent='Your appliction name')

@client.command()
async def meme(ctx):
    memes_submissions = reddit.subreddit('dankmemes').hot()
    post_to_pick = random.randint(1, 20)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)


client.run("Your token id")