import os
import requests

from PIL import Image
from io import BytesIO
from multiprocessing import Process, current_process

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse(url, amount, name):
    complete_url = '{url}/{id}.png'

    for x in range(amount[0], amount[1]):
        print('[{process}]: Parsing image #{img_id}'.format(process=current_process().name, img_id=x))
        try:
            response = requests.get(complete_url.format(url=url, id=x), stream=True)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image.save(os.path.join(BASE_DIR, 'media/images/{name}/{id}.png'.format(name=name, id=x)))
            else:
                print('Could not save image #{img_id} because of '
                      'response status {status}'.format(img_id=x, status=response.status_code))
        except Exception as exc:
            print(exc)


if __name__ == '__main__':
    image_url = ''
    image_amount = [0, 0]
    image_process = Process(target=parse, args=(image_url, image_amount, 'collection'), name='Image Process')
    image_process.start()
