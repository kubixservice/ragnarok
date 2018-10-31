import os
import codecs
import binascii
import calendar
from io import BytesIO
from PIL import Image

from rest_framework import serializers

from core.GRF.gat import Gat
from alfheimproject.settings import BASE_DIR, CONFIG


class GuildEmblemField(serializers.Field):
    GUILD_EMBLEM_PATH = 'static/guilds/icons/{id}.png'

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        # get guild_id
        guild_id = value[0]

        # Check if an emblem already exists for the current guild
        if os.path.isfile(os.path.join(BASE_DIR, self.GUILD_EMBLEM_PATH.format(id=guild_id))):
            return serializers.Hyperlink('{url}/{path}'.format(url=CONFIG['server']['conf']['server_domain'],
                                                               path=self.GUILD_EMBLEM_PATH.format(id=guild_id)), None)
        else:
            # if not - create
            # get blob data [emblem_data]
            emblem_data = value[1]
            if emblem_data:
                # generate guild emblem string based on blob in our db
                binary_string = binascii.unhexlify(emblem_data)
                binary_string = codecs.decode(binary_string, "zlib")
                # make emblem transparent
                img = Image.open(BytesIO(binary_string))
                img = img.convert("RGBA")
                items = img.getdata()

                png_transparent = []
                for item in items:
                    if item[0] == 255 and item[1] == 0 and item[2] == 255:
                        png_transparent.append((255, 255, 255, 0))
                    else:
                        png_transparent.append(item)

                img.putdata(png_transparent)
                # save new emblem into emblem's path
                img.save(self.GUILD_EMBLEM_PATH.format(id=guild_id), "PNG")
                return serializers.Hyperlink('{url}/{path}'.format(url=CONFIG['server']['conf']['server_domain'],
                                                                   path=self.GUILD_EMBLEM_PATH.format(
                                                                       id=guild_id)), None)
        # No emblem found for this guild
        return None


class GatField(serializers.Field):
    GAT_PATH = 'media/grf/gat/{map_name}.gat'
    MINIMAP_PATH = 'media/grf/minimap/{map_name}_{x}_{y}.png'

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        map_name, x, y = value[0], value[1], value[2]
        # check if map image already exists
        if not os.path.isfile(os.path.join(BASE_DIR, self.MINIMAP_PATH.format(map_name=map_name, x=x, y=y))):
            gat = Gat(self.GAT_PATH.format(map_name=map_name), scale=2)
            gat(x=x, y=y, map_name=map_name, path=self.MINIMAP_PATH)
        # return path to it
        return serializers.Hyperlink('{url}/{path}'.format(url=CONFIG['server']['conf']['server_domain'],
                                                           path=self.MINIMAP_PATH.format(map_name=map_name,
                                                                                         x=x, y=y)), None)


class ClassNameField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class DayOfWeekField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        value = calendar.day_name[value]
        return value
