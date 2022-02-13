# coding=utf8

import discord
import leagueApiHandler
import json
import time
import requests

# Open dictionary from data.json to fp, then load data into "data" variable
with open(r'C:\Users\malwt\eclipsePhoton-workspace\discord\data.json') as fp:
    data = json.load(fp)

# Discord token
TOKEN = 'NjcyMTU0MTk1NDE1MDA3MjQy.XjHWxg.u2qE9vyFxgyTsOp-5aL87ADAw2w'

# Invite URL for Discord bot = https://discordapp.com/oauth2/authorize?&client_id=672154195415007242&scope=bot&permissions=8

client = discord.Client()


@client.event
async def on_message(message):
    # Check if the author is the bot to avoid auto replies
    if message.author == client.user:
        return

    if message.content.startswith('*help'):
        # Help command, sends available commands
        msg="```- *reg : Registrar tu nombre de invocador.\n- *ranks <nombre> : Solicitar información de partida del nombre dado.\n- *ranks : Solicitar información de tu partida con tu nombre registrado.\n- *dp <url> : Cambiar la DP con url.\n- *dp <imagen> : Cambiar la DP a la imagen```"
        await client.send_message(message.channel, msg)

    if message.content.startswith('*region '):
        # Change region for league API
        message2 = message.content[7:]
        leagueApiHandler.regionn(message2)
        
    if message.content.startswith('up'):
        # Check if bot is up, check delay
        msg = 'Up {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('*reg '):
        # Register summoner name for discord account
        # This is done so each user can register their summoner name
        # When they call *ranks with no summoner name, it will default to their registered summoner name (if available)
        data[message.author.id] = message.content[5:]
        with open('C:\\Users\malwt\eclipsePhoton-workspace\discord\data.json','w') as fp:
            json.dump(data, fp)
            await client.send_message(message.channel, ':thumbsup:')

            
    if message.content.startswith('*ranks'):
        # Get ranks from active game
        message2 = message.content[6:]
        if len(message2)==0: # If there's no summoner name, try to look it up from *reg command
            try:
                # Check if available
                data[message.author.id] 
                # Use if available
                message2 = data[message.author.id] 
            except Exception as error: 
                # If not available, ask for register and exit
                await client.send_message(message.channel, 'Regístrate con *reg <nombre>')
                return
        await client.send_message(message.channel, message2)
        if(len(message2)>1):msg=leagueApiHandler.rangos(message2).format(message)#w.rangos(message2)
        await client.send_message(message.channel, msg)
    
    if message.content.startswith('nice'):
        # Dumb check to see if it can identify any message
        msg = 'n  i  c  e'.format(message)
        await client.send_message(message.channel, msg)
        
    if message.content.startswith('*dp') and (message.author.id=='183189874864685057' or message.author.id=='178497114823720961'):
        # Change display picture, only available for hardcoded discord ids
        if not message.attachments:
            # If there's noa ttachment, check if url is passed and use it
            rest = message.content[3:]
            file = requests.get(rest)
            open('dp.png', 'wb').write(file.content)
            with open('dp.png','rb') as file1:
                await client.edit_profile(avatar=file1.read())
            
        else:
            # If there's an attachment, use it
            url = message.attachments[0]["url"]
            #await client.send_message(message.channel, url)

            file = requests.get(url)
            open('dp.png', 'wb').write(file.content)
            with open('dp.png','rb') as file1:
                await client.edit_profile(avatar=file1.read())
                
                
    if message.content.startswith('ydv'):
        # Dumb check to try out emojis and custom emotes
        msg1 = 'looking left because you didnt treat me right'.format(message)
        em1 = '<:left1:677540202910318632>'.format(message)
        msg2 = 'looking right because you left'.format(message)
        em2=  '<:right1:677540214628941833>'.format(message)
        msg3 = 'looking forward because you left me behind'.format(message)
        em3 = '<:forward1:677540233079947284>'.format(message)
        msg4 = 'looking away because you didnt stay'.format(message)
        em4 = '<:away1:677540243330564119>'
        msg5 = 'looking back because youre in my way'.format(message)
        em5 = '<:back1:677540254302994432>'.format(message)
        msgs = [msg1,msg2,msg3,msg4,msg5]
        ems = [em1,em2,em3,em4,em5]
        for i in range (0,5):
            await client.send_message(message.channel, msgs[i])
            await client.send_message(message.channel, ems[i])
            time.sleep(2)
        
    if message.content.startswith('uwu'):
        # Dumb check to try spoiler discord format options
        msg = '||uwu||'.format(message)
        await client.send_message(message.channel, msg)
        

    if message.content.startswith('*stop'):
        # Stop the bot
        msg=':wave: bye'
        await client.send_message(message.channel, msg)
        await client.logout()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)