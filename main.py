import discord
import random
#257304967981826049
TOKEN = 'XXXXXXXXXXXX'

client = discord.Client()
@client.event
async def on_member_join(member):
    if member.guild.name == 'ProgChamp':
        lista = []
        lista.append(member.guild.get_role(694702413780877362))
        await member.edit(roles=lista)
        msg = 'Alterei o cargo do '+ member.name + ' para o de '+str(lista[0])
        await member.guild.get_channel(694702150563004468).send(msg)
        
    
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.guild.roles)
    print(message.author)
    print(message)
    if(message.content.startswith('!')):
        if  (message.author.name+'#'+message.author.discriminator) == "Gumb#5399":
            msg = 'Vai se foder Gumb'
            await message.channel.send(msg)
        elif (message.author.name+'#'+message.author.discriminator) != "Filipe#2783":
            msg = 'Vc nao é o Filipe vc é  {0.author.mention}'.format(message)
            await message.channel.send(msg)
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
                        target = random.choice(i.members)
                        if not target:
                            msg = 'Ta querendo me fuder? Tem ninguem nesse chat'
                        else:
                            msg = 'A roleta rodou e o otario da vez foi o '+ target.name + '! Ja era ramelão!'
                            await target.edit(voice_channel=None)
                        break
                if not target:
                    msg = 'Não consegui encontrar a sala que você disse! Deus me deu duas bolas, nenhuma de cristal!'
        
                await message.channel.send(msg)

        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)