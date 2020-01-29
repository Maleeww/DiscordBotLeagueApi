# coding=utf8

import discord
#import w
#import json
#import time
import requests
#Abrimos el diccionario de data.json en fp y hacemos load en una variable
#with open(r'C:\Users\malwt\eclipsePhoton-workspace\discord\data.json') as fp:
#    data = json.load(fp)
TOKEN = 'NjcyMTU0MTk1NDE1MDA3MjQy.XjHWxg.u2qE9vyFxgyTsOp-5aL87ADAw2w'

# URL = https://discordapp.com/oauth2/authorize?&client_id=672154195415007242&scope=bot&permissions=8

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return


    if message.content.startswith('*au'):
        channel = message.author.state.channel
        msg = "Started".format(message)
        await client.send_message(message.channel, msg)
        async def on_reaction_add(r1, u1):
            if r1.message == msg and r1.emoji.name=='M':
                #r1.user y de ahi sacas voicestate, desde el voicestate sacas lista de usuarios
                msg1="mute".format(message)
                await client.send_message(message.channel, msg1)
         
        async def on_reaction_remove(r2, u2):
            if r2.message == msg and r2.emoji.name=='M':
                msg2="unmute".format(message)
                await client.send_message(message.channel, msg2)

    if message.content.startswith('*help'):
        #msg="```- *reg : Registrar tu nombre de invocador.\n- *ranks <nombre> : Solicitar información de partida del nombre dado.\n- *ranks : Solicitar información de tu partida con tu nombre registrado.\n- *dp <url> : Cambiar la DP con url.\n- *dp <imagen> : Cambiar la DP a la imagen```"
        #await client.send_message(message.channel, msg)
        return
        
    if message.content.startswith('*dp') and (message.author.id=='183189874864685057' or message.author.id=='178497114823720961'):
        if not message.attachments:
            rest = message.content[3:]
            file = requests.get(rest)
            open('dp.png', 'wb').write(file.content)
            with open('dp.png','rb') as file1:
                await client.edit_profile(avatar=file1.read())
            
        else:
            url = message.attachments[0]["url"]
            #await client.send_message(message.channel, url)

            file = requests.get(url)
            open('dp.png', 'wb').write(file.content)
            with open('dp.png','rb') as file1:
                await client.edit_profile(avatar=file1.read())


    if message.content.startswith('*stop'):
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