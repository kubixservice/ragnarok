import os
import codecs
import binascii
import calendar
from io import BytesIO
from PIL import Image
from rest_framework import serializers
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
                # generate .bmp guild emblem based on blob in our db
                binary_string = binascii.unhexlify(emblem_data)
                binary_string = codecs.decode(binary_string, "zlib")
                # make emblem transparent
                img = Image.open(BytesIO(binary_string))
                img = img.convert("RGBA")
                datas = img.getdata()

                png_transparent = []
                for item in datas:
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


class VendingTitleFields(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value
