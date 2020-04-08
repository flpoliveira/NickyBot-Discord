import discord
import random
import os
from datetime import datetime, timedelta
from discord.ext import commands, tasks

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

eventos_id = 1
eventos = []

class Evento:
    def __init__(self, title, description, date, ctx):
        global eventos_id
        self.id = eventos_id
        eventos_id += 1
        self.title = title
        self.description = description
        self.date = date
        self.insertedTime = datetime.now()
        self.ctx = ctx

        d = self.date - self.insertedTime
        delta = timedelta(days=1)
        if(d <=  delta):
            self.warning24h = False
            delta = timedelta(minutes=60)
            if(d <= delta):
                self.warning60m = False
                delta = timedelta(minutes = 15)
                if(d <= delta):
                    self.warning15m = False
                else:
                    self.warning15m = True
            else:
                self.warning60m = True
                self.warning15m = True
        else:
            self.warning24h = True
            self.warning60m = True
            self.warning15m = True

        self.warningNow = True
        

    async def toString(self):
        emb = discord.Embed(
                    title='Evento adicionado com sucesso',
                    colour = discord.Colour.green()
                )
        emb.set_author(name=str(self.ctx.message.author))
        emb.add_field(name='Titulo do Evento', value=self.title, inline=True)
        emb.add_field(name='Numero do Evento', value=self.id, inline=True)
        emb.add_field(name='Decrição do Evento', value=self.description, inline=False)
        emb.add_field(name='warning24h', value=str(self.warning24h), inline=False)
        emb.add_field(name='warning60m', value=str(self.warning60m), inline=False)
        emb.add_field(name='warning15m', value=str(self.warning15m), inline=False)
        emb.add_field(name='warningNow', value=str(self.warningNow), inline=False)
        emb.add_field(name='Data', value=self.date.strftime('%d/%m/%Y %H:%M'))
        emb.set_footer(text='Evento cadastrado em: '+ self.insertedTime.strftime('%d/%m/%Y %H:%M'))
        await self.ctx.send(embed=emb)

    async def checkTime(self):
        localtime = datetime.now()
        d = self.date - localtime
        titulo = None
        cor = None
        if self.warning24h:
            delta = timedelta(days=1)
            if(d <= delta):
                titulo = "Um evento está marcado para amanha"
                cor = discord.Colour.green()
                self.warning24h = False
        elif self.warning60m:
            delta = timedelta(hours=1)
            if(d <= delta):
                titulo = "Um evento está marcado para daqui uma hora"
                cor = discord.Colour.orange()
                self.warning60m = False
        elif self.warning15m:
            delta = timedelta(minutes=15)
            if(d <=  delta):
                titulo = "Um evento está marcado para daqui 15 minutos"
                cor = discord.Colour.red()
                self.warning15m = False
        elif self.warningNow:
            if(localtime >= self.date):
                titulo = "Um evento está acontecendo agora"
                cor = discord.Colour.blue()
                self.warningNow = False
        if titulo:
            emb = discord.Embed(
                        title=titulo,
                        colour = cor
                    )
            emb.set_author(name=str(self.ctx.message.author))
            emb.add_field(name='Titulo do Evento', value=self.title, inline=True)
            emb.add_field(name='Numero do Evento', value=self.id, inline=True)
            emb.add_field(name='Decrição do Evento', value=self.description, inline=False)
            emb.add_field(name='Data', value=self.date.strftime('%d/%m/%Y %H:%M'))
            emb.set_footer(text='Evento cadastrado em: '+ self.insertedTime.strftime('%d/%m/%Y %H:%M'))

            await self.ctx.send(embed=emb)

        
        


               
           

client = commands.Bot(command_prefix = ';')


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
    #drink_water.start()
    checkEvent.start()

@client.command()
async def minecraft(ctx):
    
    emb = discord.Embed(
                    title='Pingando o Servidores de minecraft',
                    colour = discord.Colour.green()
                )
    emb.add_field(name='Server do Peter ', value='179.235.247.184:25565', inline=True)

    hostname = "179.235.247.184" #example
    response = os.system("ping -p 25565 -c 1 " + hostname + " &")

    #and then check the response...
    if response == 0:
        emb.add_field(name='Status', value=':white_check_mark:', inline=True)
    else:
        emb.add_field(name='Status', value=':x:', inline=True)
  
    await ctx.send(embed=emb)

@client.command()
async def listEvents(ctx):
    
    if len(eventos) == 0:
        emb = discord.Embed(
                title='Listando todos os eventos',
                description='Não há eventos cadastrados :confused:',
                colour = discord.Colour.blue()
            )
    else:
        emb = discord.Embed(
                title='Listando todos os eventos',
                colour = discord.Colour.blue()
            )
        for ev in eventos:
            emb.add_field(name='Id #', value=ev.id, inline=True)
            emb.add_field(name='Autor', value=str(ev.ctx.message.author), inline=True)
            emb.add_field(name='Data', value=ev.date.strftime('%d/%m/%Y %H:%M'), inline=True)
            # if ev.warningNow:
            #     emb.add_field(name='Status', value=':white_check_mark:', inline=True)
            # else:
            #     emb.add_field(name='Status', value=':x:', inline=True)
    await ctx.send(embed= emb)
        
    
   
@client.command()
async def test(ctx):
    localtime = datetime.now().strftime('%d/%m/%Y')
    emb = discord.Embed(
                title='Um evento começara em 15 minutos',
                colour = discord.Colour.red()
            )
    emb.set_author(name=str(ctx.message.author))
    emb.add_field(name='Titulo do Evento', value='Evento X', inline=True)
    emb.add_field(name='Numero do Evento', value='15', inline=True)
    emb.add_field(name='Decrição do Evento', value='Vamo jogar minecraft caralho', inline=False)
    emb.set_footer(text='Evento cadastrado em: '+ localtime)

    await ctx.send(embed=emb)
@client.command()
async def ping(ctx):
    author = ctx.message.author
    if checkGumb(author, ctx.message.guild):
        await ctx.send('Sai daqui '+author.mention+' !')
        return
    else:
        await ctx.send(f'Pong {round(client.latency * 1000)}ms')

@client.command()
async def addEvent(ctx, title, description, date):
    d = datetime.strptime(date, '%d/%m/%Y %H:%M')
    localtime = datetime.now()
    if(localtime > d):
        await ctx.send('Evento com data do passado! Não foi adicionado')
        return
    aux = Evento(title, description, d, ctx)
    eventos.append(aux)
    await aux.toString()
    
   

@client.command()
async def medesmuta(ctx):
    await ctx.message.author.edit(mute=False)
    await ctx.send(ctx.message.author.mention + ' foi desmutado!')


@client.command()
async def roletarussa(ctx, *, args):
    author = ctx.message.author
    if checkGumb(author, ctx.message.guild):
        await ctx.send('Sai daqui '+author.mention+' !')
        return
    else:
        target = None
        for i in ctx.message.guild.voice_channels:
            if i.name == args:
                if len(i.members) > 1:
                    if ctx.message.author not in i.members:
                        await ctx.send('Tu nem ta no chat e quer tirar os outros? Vai se fuder!')
                        return
                    else:
                        target = random.choice(i.members)
                        await target.edit(voice_channel=None)
                        await ctx.send('A roleta rodou e o otario da vez foi o '+target.mention+'! Já era ramelão!')
                        return
                else:
                    await ctx.send('Não tem gente suficiente nessa sala.')
                    return
        if not target:
            await ctx.send('Não consegui encontrar a sala que você disse! Deus me deu duas bolas, nenhuma de cristal!')
        


@client.command()
async def porrada(ctx, *, args):
    if checkGumb(ctx.message.author, ctx.message.guild):
        await ctx.send('Sai daqui '+ctx.message.author.mention+' !')
        return
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


@tasks.loop(seconds=60)
async def checkEvent():
    print("Checando os eventos")
    for ev in eventos:
        await ev.checkTime()
        

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