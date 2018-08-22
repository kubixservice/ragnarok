import requests
import feedparser
from bs4 import BeautifulSoup

from alfheimproject.settings import CONFIG


def get_medium_posts():
    page = requests.get("https://medium.com/feed/@{user}".format(user=CONFIG['api']['medium']['username']))
    rss = feedparser.parse(page.content)

    posts = []
    for i, post in enumerate(rss.entries):
        soup = BeautifulSoup(post.summary, "html.parser")

        new_post = {
            "title": post.title,
            "img_url": soup.find("img")["src"],
            "summary": soup.find("p").text,
            "published": post.published,
            "link": post.link
        }

        if "https://cdn-images-1.medium.com" in soup.find("img")["src"]:
            posts.append(new_post)
    return posts
