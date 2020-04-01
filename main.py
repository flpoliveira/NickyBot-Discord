import discord
import random

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
contadorGumbChato = 0

client = discord.Client()
@client.event
async def on_member_join(member):
    if member.guild.name == 'ProgChamp':
        lista = []
        lista.append(member.guild.get_role(id=694702413780877362))
        await member.edit(roles=lista)
        msg = 'Alterei o cargo do '+ member.name + ' para o de '+str(lista[0])
        await member.guild.get_channel(694702150563004468).send(msg)
        
    
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    global contadorGumbChato
    print(message.guild.roles)
    print(message.author)
    print(message)

    if message.content.startswith('!gumb'):
            target = message.guild.get_member_named('Gumb')
            if not target:
                msg = 'O caralho, não to achando o Gumb!!'
            else:
                msg = 'É Gumb... Alguém ficou com pena de vc! Vou te desbloquear!'
                await message.channel.set_permissions(target, read_messages=True,
                                                send_messages=True)
            
            await message.channel.send(msg)
            
    if(message.content.startswith('!')):
        if(message.author.name+'#'+message.author.discriminator) == "Gumb#5399":
            print(contadorGumbChato)
            contadorGumbChato += 1
            if(contadorGumbChato > 3):
                await message.channel.set_permissions(message.author, read_messages=True,
                                                      send_messages=False)
                msg = 'Gumb bloqueado'
                contadorGumbChato = 0
                await message.channel.send(msg)
            else:
                msg = 'Vai se foder Gumb'
                await message.channel.send(msg)
        # elif (message.author.name+'#'+message.author.discriminator) != "Filipe#2783":
        #     msg = 'Vc nao é o Filipe vc é  {0.author.mention}'.format(message)
        #     await message.channel.send(msg)
        else:
            if message.content.startswith('!hello'):
                msg = 'Hello {0.author.mention}'.format(message)
                print(message.author)
                print(message)
                await message.channel.send(msg)

            if message.content.startswith('!mutar'):
                x = message.content.split(' ', 1)
                target = message.guild.get_member_named(x[1])
                if not target:
                    msg = 'Foi mal mestre Filipe, não encontrei esse cria não :disappointed_relieved:'
                else:
                    msg = 'Calaboca ai ' + target.name +' ja ta falando merda ja!'
                    await target.edit(mute=True)
                await message.channel.send(msg)
               

            if message.content.startswith('!desmutar'):
                x = message.content.split(' ', 1)
                target = message.guild.get_member_named(x[1])
                if not target:
                    msg = 'Foi mal mestre Filipe, não encontrei esse cria não :disappointed_relieved:'
                else:
                    msg = 'Pode falar ai ' + target.name + '!'
                    await target.edit(mute=False)
                await message.channel.send(msg)
            
            if message.content.startswith('!deaf'):
                x = message.content.split(' ', 1)
                target = message.guild.get_member_named(x[1])
                if not target:
                    msg = 'Foi mal mestre Filipe, não encontrei esse cria não :disappointed_relieved:'
                else:
                    msg = 'Vai fica sem ouvir ' + target.name + '!'
                    await target.edit(deafen=True)
                await message.channel.send(msg)
            
            if message.content.startswith('!undeaf'):
                x = message.content.split(' ', 1)
                target = message.guild.get_member_named(x[1])
                if not target:
                    msg = 'Foi mal mestre Filipe, não encontrei esse cria não :disappointed_relieved:'
                else:
                    msg = 'Agora pode ouvir ' + target.name + '!'
                    await target.edit(deafen=False)
                await message.channel.send(msg)
            
            if message.content.startswith('!kick'):
                x = message.content.split(' ', 1)
                target = message.guild.get_member_named(x[1])
                if not target:
                    msg = 'Foi mal mestre Filipe, não encontrei esse cria não :disappointed_relieved:'
                else:
                    msg = 'Vai com Deus ' + target.name + '!'
                    await target.edit(voice_channel=None)
                await message.channel.send(msg)

            
                
            
            if message.content.startswith('!roletarussa'):
                x = message.content.split(' ', 1)
                target = None
                for i in message.guild.voice_channels:
                    if i.name == x[1]:
                        if len(i.members) > 1:
                            if message.author not in i.members:
                                target = 1
                                msg = 'Tu nem ta no chat e quer tirar os outros? Vai se fuder!'
                            else:
                                target = random.choice(i.members)
                                msg = 'A roleta rodou e o otario da vez foi o '+ target.name + '! Ja era ramelão!'
                                await target.edit(voice_channel=None)
                        else:
                            target = 1
                            msg = 'Ta querendo me fuder? Tem ninguem nesse chat, no maximo uma cabeça'
                        break
                if not target:
                    msg = 'Não consegui encontrar a sala que você disse! Deus me deu duas bolas, nenhuma de cristal!'
        
                await message.channel.send(msg)
            
            if message.content.startswith('!porrada'):

                x = message.content.split(' ', 1)
                target = message.guild.get_member_named(x[1])
                if target == message.author:
                    msg = 'Nao vou deixa você bater em si mesmo! Eu vou te quebrar na porrada!\n'
                    msg + ':punch::punch::punch::punch::punch::punch::punch:\n'
                    msg = msg + client.user.mention + ' deu 30 tiro de ak47 no '+ message.author.mention + '\n'
                    msg = msg + 'Mas no final quem ganhou foi o '+client.user.mention+' :trophy::trophy:'
                    await message.channel.send(msg)
                else:
                    mensagensAleatorios = []
                    mensagensAleatorios.append('')
                    mensagensAleatorios.append(' chute no saco nao')
                    mensagensAleatorios.append(' de arma não vale seu lixo!')
                    mensagensAleatorios.append(' tomou uma no queixo')
                    mensagensAleatorios.append(' levo uma facada no pinto')
                    if not target:
                        msg = 'Foi mal mestre Filipe, não encontrei esse cria não :disappointed_relieved:'
                    else:
                        msg = message.author.mention+' chamou o '+target.mention+' para o duelo!\n'
                        msg = msg + ':punch::punch::punch::punch::punch::punch::punch:\n'
                        lista = []
                        lista.append(message.author)
                        lista.append(target)
                        vencedor = random.choice(lista)
                        mensagem = random.choice(mensagensAleatorios)
                        
                    
                        msg = msg + 'O pau ta comendo! :cloud::cloud::cloud::cloud:\n'
                        if mensagem != '':
                            eventoAleatorio = random.choice(lista)
                            msg = msg + eventoAleatorio.mention + mensagem + '\n'
                        msg = msg + 'Mas no final quem ganhou foi o '+vencedor.mention +' :trophy::trophy:'
                        await message.channel.send(msg)


               


           

        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)