import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def topla2(ctx,S1=7,S2=19):
    await ctx.send(S1+S2)


    
@bot.command()
async def topla(ctx,S3=int,S4=int):
    await ctx.send(S3/S4)

@bot.command()
async def memes(ctx):
    with open("Resimler/Z.png","rb")as f:
        ilkr=discord.File(f)
    await ctx.send(file=ilkr)
    
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():    
    url = "https://randomfox.ca/floof/"
    res = requests.get(url)
    data = res.json()
    return data['image']


@bot.command('fox')
async def fox(ctx):
    '''fox komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)


def get_dog_image_url():    
    url = "https://random.dog/woof.json"
    res = requests.get(url)
    data = res.json()
    return data["url"]


@bot.command('dog')
async def dog(ctx):
    '''fox komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

def get_pokemon_image_url():    
    url = 'https://pokeapi.co/api/v2/pokemon/ditto'
    res = requests.get(url)
    data = res.json()
    return data['sprites']


@bot.command('pokemon')
async def pokemon(ctx):
    '''duck komutunu çağırdığımızda, program ordek_resmi_urlsi_al fonksiyonunu çağırır.'''
    image_url = get_pokemon_image_url()
    await ctx.send(image_url)


bot.run("MTEzMTI2NDAwMDk0OTIzNTc0Mg.Gi0HMR.0eHQl07zpFMjtyPjgGpjhJHQPetMTqg5hPo4Ok")