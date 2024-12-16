import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send("merhaba")

@bot.command()
async def Bilgi(ctx):
    await ctx.send()

@bot.command()
async def bilgi(ctx,bilgix):
    Sozluk={"Tarkan":["Tarkan Tevetoğlu ya da sahne adıyla Tarkan (d. 17 Ekim 1972), Türk şarkıcı-şarkı yazarıdır. 1990'ların başından itibaren Türk pop müziğinde yakaladığı devamlı liste ve satış başarılarıyla Türkiye'de ve dünya çapında tanınırlık elde etti.Tarkan, Batı Almanya'nın Renanya-Palatina eyaletindeki Alzey kasabasında doğup büyüdü. 1986'da ailesiyle beraber Türkiye'ye geldi ve müziğe çocukluk yıllarında başlayan ilgisi sonucunda, lise hayatına başladığı Karamürsel'de ilk müzik eğitimini almaya başladı. İlerleyen yıllarda İstanbul Plak şirketinin sahibi Mehmet Söğütoğlu ile tanışarak şirket ile bir albüm anlaşması imzaladı."],
            "Jüpiter":["Jüpiter, Güneş Sistemi'nin en büyük gezegenidir. Güneş'ten uzaklığa göre beşinci sırada yer alır. Adını Roma mitolojisindeki tanrıların en büyüğü olan Jüpiter'den alır. Büyük ölçüde hidrojen ve helyumdan oluşmakta ve gaz devi sınıfına girmektedir."],
            "Alper Gezeravcı":["Uzaya Çıkan İlk Türk İnsandır.alalalala"]}
    
    Lale=random.choice (list(Sozluk.items()))
    await 