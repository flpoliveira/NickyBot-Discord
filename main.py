import discord
#257304967981826049
TOKEN = 'Njk0NjcwODAzMjE1NzEyMzY2.XoPBiQ.Te4Yz2OX6UX2MQVjDoeS6CdNuF8'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

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
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)