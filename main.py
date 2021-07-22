#imports
import discord
from discord.ext import commands
import asyncio
import os
from dotenv import load_dotenv, find_dotenv

#carrega o arquivo .env
load_dotenv(find_dotenv())
prefixo = os.getenv('prefixo')
token = os.getenv('token')

#setup
bot = commands.Bot(command_prefix=prefixo, case_insensitive=True)

bot.remove_command('help')


#eventos
@bot.event
async def on_ready():
    print('Estou online')


#comandos
@bot.command()
async def calc(ctx, n1, n2):
    soma = int(n1) + int(n2)
    await ctx.send(soma)

@bot.command()
async def calc_melhorada(ctx, *, expressao):
    soma = eval(expressao)
    await ctx.send(soma)
    
#help
@bot.command()
async def help(ctx):
    await ctx.send('Olá, sou o bot de testes da codify.\n**Meu prefixo nesse servidor é "."**\n\n> Criado por: jv#0001')


#comandos embed
@bot.command()
async def fale(ctx, *, frase):
    emb = discord.Embed(title='FALADOR', description=frase, color=0x4284f5, url='https://www.youtube.com/channel/UCH0iGcEvHhYnKBeTuIY0OeA')
    #emb.set_image(url='https://media.discordapp.net/attachments/851619135061491752/866036761163202600/5e450c2a3052b7464f554759b808cbfb.png?width=843&height=670')
    #emb.set_thumbnail(url='https://media.discordapp.net/attachments/851619135061491752/866036761163202600/5e450c2a3052b7464f554759b808cbfb.png?width=843&height=670')
    #emb.set_author(name='Bot da codify', icon_url='https://media.discordapp.net/attachments/851619135061491752/867562700544802816/unknown.png')
    #emb.set_footer(text='rodapé da embed', icon_url='https://media.discordapp.net/attachments/851619135061491752/867562700544802816/unknown.png')
    
    #emb.add_field(name='Campo 1', value='Texto do campo 1', inline=False)
    #emb.add_field(name='Campo 2', value='Texto do campo 2', inline=False)
    #emb.add_field(name='Campo 3', value='Texto do campo 3', inline=False)
    print('ok')
    print('ok2')
    await ctx.send(embed=emb)

#iniciaçização
bot.run(token)