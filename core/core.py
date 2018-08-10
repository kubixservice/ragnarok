import datetime
import socket
import importlib

import requests

from main_api.models import ServerHighestPeak
from alfheimproject.settings import CONFIG

models = importlib.import_module('core.{emu}.models'.format(emu=CONFIG['server']['conf']['emu_type']))


class Server(object):

    def __init__(self):
        self.server_ip = CONFIG['server']['conf']['server_ip']
        self.map_port = CONFIG['server']['conf']['map_port']
        self.char_port = CONFIG['server']['conf']['char_port']
        self.login_port = CONFIG['server']['conf']['login_port']
        self.discord_id = CONFIG['api']['discord']['guild_id']

    def get_server_status(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        map_server = sock.connect_ex((self.server_ip, self.map_port))
        char_server = sock.connect_ex((self.server_ip, self.char_port))
        login_server = sock.connect_ex((self.server_ip, self.login_port))
        sock.close()

        status = (map_server, char_server, login_server)
        map_server = True if status[0] == 0 else False
        char_server = True if status[1] == 0 else False
        login_server = True if status[2] == 0 else False

        return {
            'map_server': map_server,
            'char_server': char_server,
            'login_server': login_server,
        }

    def get_online_status(self):
        highest_peak = ServerHighestPeak.objects.get(pk=1)
        server_online = models.Char.objects.filter(online=1).all().count()
        discord_online = 0
        discord_updated = datetime.datetime.now()

        if self.discord_id:
            request = requests.get('https://discordapp.com/api/guilds/{discord_id}/embed.json'.format(
                discord_id=self.discord_id))
            response = request.json()
            discord_online = len(response['members'])
            discord_updated = datetime.datetime.now()

        return {
            'highest_peak': highest_peak.peak,
            'peak_date': highest_peak.peak_date,
            'server_online': server_online,
            'discord_online': discord_online,
            'discord_updated': discord_updated
        }


server = Server()
