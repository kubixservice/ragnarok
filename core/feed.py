import feedparser
from alfheimproject.settings import CONFIG


def feed():
    urls = CONFIG['rss']
    # response = []
    # for url in urls:
    #     parser = feedparser.parse(url['url'])
    #     response.append({
    #         url['title']: [item for item in parser.entries]
    #     })
    response = feedparser.parse(urls[0]['url'])
    return response
