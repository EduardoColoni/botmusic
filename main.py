#Importando as bibliotecas do discord para usar a funções dele e a de commandos tambem
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

from discord.ext import commands
#e depois estou importando o TOKEN que faz o script se conectar ao bot de uma variável em outro arquvio por mais segurança
from tokenbot import token



#Aqui estou definindo o argumento que vou usar para dar comandos ao bot
client = commands.Bot(command_prefix='!', intents=intents)

#Criando um evento para o bot me avisar quando ele estiver online e pronto para ser usado
@client.event
async def on_ready():
    print("O bot está pronto para uso")
    print("--------------------------")

#Criando o primeiro comando do bot para que quando eu escreva !hello o bot me retorne uma mensagem
@client.command()
async def hello(ctx, arg="hello"):
    await ctx.send("hello" + arg)

#Fazendo o bot mandar uma mensagem no canal que foi passado a ID quando alguem entra no servidor e o mencionando
@client.event
async def on_member_join(member):
    channel = client.get_channel(1086323074447704189)
    await channel.send(f"Olá, seja bem vindo, {member.mention}")

#Fazendo o bot mandar uma mensagem no canal que foi passado a ID quando alguem sair do servidor e o mencionando
@client.event
async def on_member_remove(member):
    channel = client.get_channel(1086323074447704189)
    await channel.send(f"Foi bom ter você por aqui, {member.mention}")

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Você não está em um canal de voz, por favor entre em um canal de voz primeiro antes de rodar este comando")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Eu sai do canal de voz")
    else:
        await ctx.send("Eu não estou em nenhum canal de voz")


client.run(token)
