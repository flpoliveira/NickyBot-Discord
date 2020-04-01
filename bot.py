import discord
import random
from discord.ext import commands, tasks

TOKEN = 'XXXXXXXXXXXXXXXXXXXXX'


client = commands.Bot(command_prefix = '!')


def checkGumb(user, guild):
    target = guild.get_member_named('Gumb')
    return user == target

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.guilds)
    print('------')
    drink_water.start()

@client.command()
async def ping(ctx):
    author = ctx.message.author
    if checkGumb(author, ctx.message.guild):
        await ctx.send('Sai daqui '+author.mention+' !')
        return
    else:
        await ctx.send(f'Pong {round(client.latency * 1000)}ms')

@client.command()
async def porrada(ctx, *, args):
    eventosAleatorios = [
        ' levou um chute no saco ',
        ' levou uma arma ',
        ' tomou uma facada no pinto ',
        ' chamou o pai pra briga ',
        ' é feio ',
        ' jogou um butijão de gás ',
        ' xingou a mãe do adversário ',
        ' mandou um double hangloose de pé ',
        ' trouxe uma faca para briga ',
        ' falou que a mãe do adversário toma banho pelada ',
        ''       
    ]
    target = ctx.message.guild.get_member_named(args)
    if not target:
        await ctx.send('Não consegui encontrar esse cria ai não!')
    else:
        if target == ctx.message.author:
            await ctx.send('Vai brigar contra o espelho se for pra briga com si mesmo!')
        else:
            msg = ctx.message.author.mention + ' chamou o ' + target.mention + ' para uma briga!\n'
            msg = msg + ':punch::punch::punch::punch::punch::punch::punch:\n'
            msg = msg + 'A porrada ta comendo solta!\n'
            aux = random.choice(eventosAleatorios)
            if aux !=  '':
                msg = msg + random.choice([target, ctx.message.author]).mention + aux + '\n'
            msg = msg + ':cloud::cloud::cloud::cloud::cloud::cloud::cloud:\n'
            msg = msg + 'Quem leva essa foi o '+ random.choice([target, ctx.message.author]).mention +' :trophy::trophy:' 
            await ctx.send(msg)


@client.command()
async def kick(ctx, *, args):
    
    if checkGumb(ctx.message.author, ctx.message.guild):
        await ctx.send('Sai daqui '+ctx.message.author.mention+' !')
        return
    target = ctx.message.guild.get_member_named(args)
    if not target:
        await ctx.send('Não consegui encontrar esse cria ai não!')
    else:
        tv = True
        ta = True
        for i in ctx.message.guild.voice_channels:
            if target in i.members:
                tv = False
            if ctx.message.author in i.members:
                ta = False
        if(tv):
            msg = 'O cara nem ta conectado em nenhum chat patrão! Ta de brincadeira comigo?\n'
            if(ta):
                msg = msg + ' Sorte sua que não ta conectado em nenhum chat tb! Se não tu ia rodar.'
            else:
                msg = msg +' Então vou kikar você! Vai com Deus '+ctx.message.author.mention+'!'
                await ctx.message.author.edit(voice_channel=None)
            await ctx.send(msg)
        else:
            await target.edit(voice_channel=None)
            await ctx.send('Cria '+target.mention+' eliminado com sucesso!')


@tasks.loop(seconds=(15*60))
async def drink_water():
    for guild in client.guilds:
        #if guild.id != 192415153579360256:
        target = random.choice(guild.members)
        if target != client.user:
            print(target.name + " - recebeu um aviso para tomar agua ")
            emb = discord.Embed(
                title='Beba água',
                description = 'Vá beber uma água cara',
                colour = discord.Colour.blue()
            )
            await target.send(embed=emb)
    

client.run(TOKEN)