import struct
from PIL import Image, ImageDraw

from alfheimproject.settings import logger


class Gat:
    def __init__(self, fh, scale):
        x = 0
        y = 0
        self.image = None
        self._m = dict()
        self.scale = scale
        try:
            with open(fh, 'rb') as file:
                file.read(6)
                self._xs, = struct.unpack('i', file.read(4))
                self._ys, = struct.unpack('i', file.read(4))

                n = self._xs * self._ys
                file.read(16)
                for xy in range(0, n):
                    if x not in self._m:
                        self._m[x] = dict()
                    flag, = struct.unpack('i', file.read(4))
                    if flag == 0:
                        self._m[x][y] = True
                    else:
                        self._m[x][y] = False
                    x += 1
                    if x == self._xs:
                        x = 0
                        y += 1
                    file.read(16)
        except FileNotFoundError:
            logger.error('{cls}: could not open {file} [FileNotFound]'.format(cls=self.__class__, file=fh))

    def c(self, x, y):
        if x < 0 or x >= self._xs or y < 0 or y >= self._ys:
            return False
        return self._m[x][y]

    def __call__(self, *args, **kwargs):
        xc = kwargs.get('x', 0)
        yc = kwargs.get('y', 0)
        map_name = kwargs.get('map_name')
        path = kwargs.get('path')

        self.image = Image.new('RGB', (self._xs * self.scale, self._ys * self.scale), (128, 128, 128))
        d = ImageDraw.Draw(self.image)
        x1 = ((xc * self.scale) - (self.scale / 2))
        y1 = ((yc * self.scale) - (self.scale / 2))

        for x in range(0, self._xs - 1):
            for y in range(0, self._ys - 1):
                if not self.c(x, y):
                    continue
                rx = ((x * self.scale) - (self.scale / 2),
                      (self._ys * self.scale) - (y * self.scale) - (self.scale / 2))
                ry = ((x * self.scale) + (self.scale / 2),
                      (self._ys * self.scale) - (y * self.scale) + (self.scale / 2))
                d.rectangle([rx, ry], fill=(0, 0, 0))

            d.ellipse([(x1 - 5, (self._ys * self.scale) - y1 - 5), (x1 + 5, (self._ys * self.scale) - y1 + 5)],
                      fill=(255, 0, 0),
                      outline=(0, 0, 0))

        self.image.save(path.format(map_name=map_name, x=xc, y=yc), "PNG")
