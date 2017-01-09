'''

RTL Bot
Username: RTL_Bot#4541
Client ID: 171657885892345856
<@171658665537830913>
'''

import time
import discord
import asyncio
import threading
import random
import math as m
from game import game

client = discord.Client()
def read_stats():
    players = dict()
    f = open('stats.txt')
    server_id = f.readline().strip()
    print(server_id)
    server = client.get_server(server_id)
    print(server)
    for line in f:
        line = line.strip().split(' | ')
        member = server.get_member(line[0])
        players.update({member:int(line[1])})
    f.close()
    return players


all_games = dict()
all_players = dict()

@client.event
@asyncio.coroutine
def on_ready():
    '''
    global all_players
    all_players = read_stats()
    print(all_players)
    '''

@client.event
@asyncio.coroutine
def on_message(message):
    if message.content.lower().startswith('!host') and\
       len(message.content.lower().split(' ')) == 2:
        if not message.author.voice.voice_channel == None:
            channel1 = client.get_channel('267898680319803392')
            if len(channel1.voice_members) > 0 or len(all_games) > 0:
                yield from client.send_message(message.channel, 'There is a game already in progress.')
            elif message.author.voice.voice_channel.name == 'Lobby':
                game1 = game(message, client)
                all_games.update({game1.name:game1})
                yield from game1.join_game()
                all_games.pop(game1.name)
            else:
                yield from client.send_message(message.channel, 'Please join the lobby voice channel.')
        else:
            yield from client.send_message(message.channel, 'Please join the lobby voice channel.')
'''
    elif message.content.lower().startswith('!money'):
        if message.author in all_players:
            text = 'You have ' + str(all_players[message.author]) + ' :gem:'
            yield from client.send_message(message.channel, text)
        else:
'''



client.run('MTcxNjU4NjY1NTM3ODMwOTEz.Cv4X0A.HdTZvHj5Z807U1AmsFMp0upeOPY')



