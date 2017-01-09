import discord
import time
import asyncio
import random

class game(object):
    def __init__(self, message, client):
        self.contents = message.content.split(' ')
        self.channel = message.channel
        self.host = message.author
        self.client = client
        self.name = self.contents[1]
        self.timer = 10
        self.players = [self.host]


    #For team games
    async def create_game(self):
        await self.client.send_message(self.channel,'Game starting!')
        random.shuffle(self.players)
        team1 = self.players[0:len(self.players)//2]
        team2 = self.players[len(self.players)//2:len(self.players)]
        teams = [('Team 1', team1), ('Team 2', team2)]
        for team in teams:
            player_list = team[0] + ':\n'
            for name in team[1]:
                player_list += name.mention + '\n'
            await self.client.send_message(self.channel, player_list)
        return team1, team2

    async def move_players(self, team1, team2):
        channel1 = self.client.get_channel('267898680319803392')
        for player in team1:
            await self.client.move_member(player, channel1)
        channel2 = self.client.get_channel('267898761651421195')
        for player in team2:
            await self.client.move_member(player, channel2)


    async def join_game(self):
        await self.client.send_message(self.channel, 'Game queue started.')
        async def add_players():
            while True:
                wait_for_msg = '!join ' + self.name
                response = await self.client.wait_for_message(content=wait_for_msg)
                if not response.author.voice.voice_channel == None:
                    if response.author.voice.voice_channel.name == 'Lobby':
                        if not response.author in self.players:
                            self.players.append(response.author)
                            joined_msg = response.author.mention + ' has joined the game ' + '**' + self.name + '**' + '.'
                            await self.client.send_message(self.channel, joined_msg)
                        else:
                            await self.client.send_message(self.channel, 'You are already in the game.')
                else:
                    await self.client.send_message(self.channel, 'Please join the lobby voice channel.')
        try:
            await asyncio.wait_for(add_players(), timeout=self.timer)
        except asyncio.TimeoutError:
            pass

        reroll = True
        valid_response = True
        while reroll == True:
            if valid_response == True:
                team1, team2 = await self.create_game()
            await self.client.send_message(self.channel, 'Are these teams ok? Only the host may respond. !y for yes, !n for no.')
            response = await self.client.wait_for_message(author=self.host)
            if response.content == '!y':
                reroll = False
            elif response.content == '!n':
                valid_response = True
            else:
                await self.client.send_message(response.channel, 'Invalid response. Send !y or !n.')
                valid_response = False
        await self.move_players(team1, team2)


'''

    #For blackjack
    async def blackjack(self):
        await self.client.send_message(self.channel, 'Game beginning!')


'''
    
        

