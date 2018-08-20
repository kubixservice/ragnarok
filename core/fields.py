import os
import codecs
import binascii

from rest_framework import serializers
from alfheimproject.settings import BASE_DIR, CONFIG


class GuildEmblemField(serializers.Field):
    GUILD_EMBLEM_PATH = 'static/guilds/icons/{id}.bmp'

    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        # get guild_id
        guild_id = value[0]

        # Check if emblem for current guild already exists
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
                # write new emblem into emblem's path
                with open(self.GUILD_EMBLEM_PATH.format(id=guild_id), 'wb') as f:
                    f.write(binary_string)
                    f.close()
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
