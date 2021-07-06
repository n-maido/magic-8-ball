import discord
import os
from dotenv import load_dotenv

from discord.ext import commands
from random import randint

load_dotenv()

client = commands.Bot(command_prefix='!')

embed_color=0xD13CDE
fortunes = ['That\'s weird question', 'Totally', 'Sleep on it', 'Go for it', 'No!']
horoscopes = ['You should take risks today', 'Danger is near', 'Watch out for food poisoning']

#do stuff
@client.event
async def on_ready():
    print("We are online")

    general_channel = client.get_channel(824031386515537953)
    await general_channel.send("Hello!")

@client.command(name='magic8')
async def magic8(ctx):
    info_embed = discord.Embed(title='The Magic 8-Ball has been summoned', description='', color=embed_color)

    info_embed.add_field(name='Want to see your future?', value='Type !fortune', inline=False)

    info_embed.add_field(name='Want to a private horoscope?', value='Click 🔮', inline=False)

    info_embed.set_thumbnail(url='https://media.giphy.com/media/3o6ozoD1ByqYv7ARIk/giphy.gif')

    info_message = await ctx.send(embed=info_embed)
    await info_message.add_reaction('🔮')

@client.command(name='fortune')
async def fortune(ctx, *question):
    if len(question) == 0:
        await ctx.send('I need you to ask a question!')

    index = randint(0, len(fortunes)-1)

    fortune_embed = discord.Embed(title=fortunes[index], description='', color=embed_color)

    await ctx.send(embed=fortune_embed)

@client.event
async def on_reaction_add(reaction, user):
    if user == client.user:
        return
        
    if reaction.emoji == '🔮':
        index = randint(0, len(horoscopes)-1)

        horoscope_embed = discord.Embed(title=horoscopes[index], description='', color=embed_color)

        await user.send(embed=horoscope_embed)

BOT_TOKEN = os.getenv("TOKEN")
client.run(BOT_TOKEN)